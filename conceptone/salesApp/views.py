from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from salesApp.models import SaleOrder, SaleInvoice, SaleOrderItem, SaleInvoiceItem
from salesApp.forms import SaleInvoiceSoForm, SaleInvoiceNewForm, SaleOrderForm, SaleOrderItemForm, SaleInvoiceItemForm, SelectItemFromSo, invoice_item_formset, ViewInvoiceForm, InvoiceSearchForm, SaleOrderSearchForm
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                    CreateView, UpdateView, DetailView, FormView,)
# Create views
class CreateSaleOrder(CreateView):
    model = SaleOrder
    form_class = SaleOrderForm
    template_name = 'salesApp/createsaleorder.html'
    def get_success_url(self):
        return reverse_lazy('salesApp:addsaleorderitems',kwargs={'pk':self.object.pk})

class AddSaleOrderItems(CreateView):
    model = SaleOrderItem
    form_class = SaleOrderItemForm
    template_name = 'salesApp/soadditem.html'
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['so'] = get_object_or_404(SaleOrder, pk=self.kwargs['pk'])
        context['items'] = SaleOrderItem.objects.filter(sale_order=self.kwargs['pk'])
        return context
    def form_valid(self,form):
        line_item = form.save(commit=False)
        line_item.sale_order = get_object_or_404(SaleOrder, pk=self.kwargs['pk'])
        current_obj = SaleOrderItem.objects.filter(sale_order=line_item.sale_order).order_by('-so_line_number').first()
        if current_obj !=None:
            new_line_number = (current_obj.so_line_number) + 1
        else:
            new_line_number = 1
        line_item.so_line_number = new_line_number
        line_item.total_price = line_item.unit_price*line_item.order_quantity
        line_item.tax_amount = line_item.tax_rate.tax_value*line_item.total_price
        line_item.available_quantity = line_item.order_quantity
        line_item.save()
        line_item.sale_order.CalculateSoTotal()
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('salesApp:addsaleorderitems',kwargs={'pk':self.object.sale_order.pk})

class ListSaleOrders(FormView):
    form_class = SaleOrderSearchForm
    template_name = 'salesApp/list_saleorders.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['object_list'] = SaleOrder.objects.all()
        for items in context['object_list']:
            items.CalculateSoTotal()
        return context

def SaleOrderQuery(request):
    data = request.GET
    query_result = SaleOrder.objects.all()
    if data['customer'] != '':
        query_result = query_result.filter(customer__customer_name__icontains=data['customer'])
    if data['project'] != '':
        query_result = query_result.filter(project__project_name__icontains=data['project'])
    if data['so_date'] != '':
        print(data['so_date'])
        query_result = query_result.filter(customer_po_date__range=[(data['so_date']),(data['so_date'])])
    if data['so_number'] != '':
        query_result = query_result.filter(so_number__icontains=data['so_number'])
    new_html_table = render_to_string('salesApp/tables/list_saleorderstable.html',{'object_list':query_result})
    return HttpResponse(new_html_table)

class CreateSoInvoice(FormView):
    form_class = SaleInvoiceSoForm
    template_name = 'salesApp/createsoinvoice.html'
    def form_valid(self,form):
        self.so = form.cleaned_data['sale_order']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('salesApp:selectsiitemfromso',kwargs={'pk':self.so.pk})

class SelectSaleInvoiceItemsFromSo(TemplateView):
    template_name = 'salesApp/selectsiitemfromso.html'
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        self.sonumber = self.kwargs['pk']
        context['so'] = get_object_or_404(SaleOrder, pk=self.kwargs['pk'])
        so_items = SaleOrderItem.objects.filter(sale_order=self.kwargs['pk'])
        context['object_list'] = so_items
        item_list = []
        for items in so_items:
            item_list.append(str(items.id))
        context['item_list'] = item_list
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args,**kwargs)
        selected_items = request.POST.getlist('selected_items')
        if not selected_items:
            print("No Items Selected")
            return HttpResponseRedirect(reverse('salesApp:selectsiitemfromso',kwargs={'pk':self.sonumber}))
        else:
            request.session['invoice-selected_item'] = selected_items
            issubset = set(selected_items) <= set(context['item_list'])
            return redirect('salesApp:createinvoiceso')

class CreateInvoiceSo(FormView):
    form_class = invoice_item_formset
    template_name = 'salesApp/createsoinvoiceitems.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        selected_items = self.request.session['invoice-selected_item']
        line_items = SaleOrderItem.objects.filter(id__in=selected_items)
        s_order = line_items.first().sale_order
        no_of_items = len(selected_items)
        formdata = {
            'form-TOTAL_FORMS': no_of_items,
            'form-INITIAL_FORMS': '0',
            'form-MAX_NUM_FORMS': '',
            }
        item_formset = invoice_item_formset(formdata)
        form_list = []
        for form in item_formset:
            element = {
                'qty_form' : form['bill_quantity'],
                'id_form' : form['id'],
                }
            form_list.append(element)
        i=0
        for items in line_items:
            items.form = form_list[i]
            i = i+1
        context['so'] = s_order
        context['formset'] = item_formset
        context['line_items'] = line_items
        return context

    def form_valid(self,form,*arg,**kwargs):
        context = self.get_context_data(**kwargs)
        sale_order = context['so']
        sale_order_item = context['line_items']
        line_item = SaleInvoiceItem()
        item_formset = invoice_item_formset(self.request.POST)
        i=0
        for form in item_formset:
            if form.is_valid():
                invoice_quantity = form.cleaned_data['bill_quantity']
                if invoice_quantity > sale_order_item[i].available_quantity:
                    messages.set_level(self.request,messages.WARNING)
                    messages.warning(self.request,"Bill Quantity Cannot be greater than Available Quantity")
                    return redirect('salesApp:createinvoiceso')
                i=i+1
        invoice = SaleInvoice()
        invoice.sale_order = sale_order
        invoice.customer = sale_order.customer
        invoice.project = sale_order.project
        invoice.si_date = datetime.now().date()
        invoice.save()
        if invoice.id:
            print('Invoice Id: '+str(invoice.id))

        i=0
        for form in item_formset:
            line_item = form.save(commit=False)
            line_item.sale_invoice = invoice
            line_item.sale_order_item = sale_order_item[i]
            line_item.tax_rate = sale_order_item[i].tax_rate
            line_item.total_price = line_item.bill_quantity*sale_order_item[i].unit_price
            line_item.tax_amount = line_item.total_price*line_item.tax_rate.tax_value
            line_item.save()
            if line_item.id:
                sale_order_item[i].ConsumeQuantity(line_item.bill_quantity)
            i=i+1

        invoice.CalculateSiTotal()
        return super().form_valid(item_formset)
    def get_success_url(self):
        return reverse('salesApp:createsoinvoice')


class ViewInvoices(FormView):
    form_class = InvoiceSearchForm
    template_name = 'salesApp/viewinvoices.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['object_list'] = SaleInvoice.objects.all()
        return context

#AJAX Calls to retriew invoices
def ViewInvoiceList(request):
    data = request.GET

    print("in django view!")
    query_result = SaleInvoice.objects.all()
    if data['customer'] != '':
        query_result = query_result.filter(customer__customer_name__icontains=data['customer'])
    if data['project'] != '':
        query_result = query_result.filter(project__project_name__icontains=data['project'])
    if data['sale_order'] != '':
        query_result = query_result.filter(sale_order__so_number__icontains=data['sale_order'])
    if data['invoice_number'] != '':
        query_result = query_result.filter(si_number__icontains=data['invoice_number'])
    new_html_table = render_to_string('salesapp/tables/viewinvoicestable.html',{'object_list':query_result})
    return HttpResponse(new_html_table)
