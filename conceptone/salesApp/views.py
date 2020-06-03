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
from salesApp.forms import SaleInvoiceSoForm, SaleInvoiceNewForm, SaleOrderForm, SaleOrderItemForm, SaleInvoiceItemForm, SelectItemFromSo, invoice_item_formset, ViewInvoiceForm, InvoiceSearchForm
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                    CreateView, UpdateView, DetailView, FormView,)
# Create your views here.
class CreateSaleOrder(CreateView):
    model = SaleOrder
    form_class = SaleOrderForm
    template_name = 'salesApp/createsaleorder.html'
    def get_success_url(self):
        return reverse_lazy('salesApp:addsaleorderitems',kwargs={'pk':self.object.pk})

# class CreateSoInvoice(CreateView):
#     model = SaleInvoice
#     form_class = SaleInvoiceSoForm
#     template_name = 'salesApp/createsoinvoice.html'
#     def form_valid(self,form):
#         so_invoice = form.save(commit=False)
#         so_invoice.si_customer = so_invoice.si_sonumber.so_customer
#         so_invoice.si_project = so_invoice.si_sonumber.so_project
#         so_invoice.save()
#         return super().form_valid(form)
#     def get_success_url(self):
#         return reverse_lazy('salesApp:addsiitemfromso',kwargs={'pk':self.object.si_sonumber.pk})

class CreateSoInvoice(FormView):
    form_class = SaleInvoiceSoForm
    template_name = 'salesApp/createsoinvoice.html'
    def form_valid(self,form):
        self.so = form.cleaned_data['sale_order']
        # self.request.session['so_num'] = self.so
        # print(self.so.pk)
        # self.form = form
        return super().form_valid(form)

    def get_success_url(self):
        # so = self.form.cleaned_data['si_sonumber']
        return reverse_lazy('salesApp:selectsiitemfromso',kwargs={'pk':self.so.pk})

class SelectSaleInvoiceItemsFromSo(TemplateView):
    template_name = 'salesApp/selectsiitemfromso.html'
    # item_list = []
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        self.sonumber = self.kwargs['pk']
        # print(self.sonumber)
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
            # print(self.kwargs['pk'])
            return HttpResponseRedirect(reverse('salesApp:selectsiitemfromso',kwargs={'pk':self.sonumber}))
        else:
            request.session['invoice-selected_item'] = selected_items
            issubset = set(selected_items) <= set(context['item_list'])
            # something went wrong page
            return redirect('salesApp:createinvoiceso')
            # print("*** After POST ***")
            # print(issubset)
            # print(selected_items)
            # print(context['item_list'])

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
        # print(item_formset)
        context['line_items'] = line_items
        return context

    # def post(self,request,*arg,**kwargs):
    #     item_formset = invoice_item_formset(request.POST)
    #     # myformset = item_formset(request.POST)
    #     if item_formset.is_valid():
    #         print("valid")
    #         for key, value in item_formset:
    #             print('Key: %s' % (key) )
    #             # print(f'Key: {key}') in Python >= 3.7
    #             print('Value %s' % (value) )
    #             # print(f'Value: {value}') in Python >= 3.7
    #     else:
    #         print("Invalid")
    #     return HttpResponseRedirect(reverse('salesApp:createsoinvoice'))

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
                    # invoice.delete()
                    # print(invoice.id)
                    return redirect('salesApp:createinvoiceso')
                i=i+1
        invoice = SaleInvoice()
        invoice.sale_order = sale_order
        invoice.customer = sale_order.customer
        invoice.project = sale_order.project
        invoice.si_date = datetime.now().date()
        if invoice.id:
            print("Nayyyy!!!!")
        invoice.save()
        if invoice.id:
            print("Yayyyy!!!!")
        print('Invoice Id: '+str(invoice.id))

        i=0
        for form in item_formset:
            line_item = form.save(commit=False)
            line_item.sale_invoice = invoice
            line_item.sale_order_item = sale_order_item[i]
            line_item.tax_rate = sale_order_item[i].tax_rate
            line_item.total_price = line_item.bill_quantity*sale_order_item[i].unit_price
            line_item.tax_amount = line_item.total_price*line_item.tax_rate.tax_value
            print('*** Saving Item ***')
            line_item.save()
            # print(sale_order_item[i])
            if line_item.id:
                sale_order_item[i].ConsumeQuantity(line_item.bill_quantity)
            i=i+1
            # print(form)
            # print(line_item)

        invoice.CalculateSiTotal()
        return super().form_valid(item_formset)
    def get_success_url(self):
        return reverse('salesApp:createsoinvoice')
#Using FormView#
###################################
# class SelectSaleInvoiceItemsFromSo(FormView):
#     # model = SaleOrderItem
#     template_name = 'salesApp/selectsiitemfromso.html'
#     form_class = SelectItemFromSo
#     def get_context_data(self,*args,**kwargs):
#         context = super().get_context_data(*args,**kwargs)
#         context['so'] = get_object_or_404(SaleOrder, pk=self.kwargs['pk'])
#         context['object_list'] = SaleOrderItem.objects.filter(so_number=self.kwargs['pk'])
#         for item in context['object_list']:
#             context['form']['selected_item'].widget.attrs['value'] = item.id
#         return context
#
#     def post(self, request, *args, **kwargs):
#         selected_items = request.POST.getlist('selected_items')
#         print(selected_items)
#         context = self.get_context_data(*args,**kwargs)
#         return self.render_to_response(context)
#
#     def form_valid(self,form):
#         selected_items = form.cleaned_data['selected_item']
#         print(selected_items)
#         return super(SelectSaleInvoiceItemsFromSo,self).form_valid(form)
#     def get_success_url(self):
#         return reverse_lazy('salesApp:selectsiitemfromso',kwargs={'pk':self.pk})
###################################



class CreateInvoiceFromSo(CreateView):
    model = SaleInvoice
    form_class = SaleInvoiceSoForm



class CreateNewInvoice(CreateView):
    model = SaleInvoice
    form_class = SaleInvoiceNewForm
    template_name = 'salesApp/createnewinvoice.html'
    def get_success_url(self):
        return reverse_lazy('salesApp:createsoinvoice')

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

class AddSaleInvoiceItems(CreateView):
    model = SaleInvoiceItem
    form_class = SaleInvoiceItemForm
    template_name = 'salesApp/siadditem.html'
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['si'] = get_object_or_404(SaleInvoice, pk=self.kwargs['pk'])
        context['items'] = SaleInvoiceItem.objects.filter(so_number=self.kwargs['pk'])
        return context
    def form_valid(self,form):
        line_item = form.save(commit=False)
        line_item.si_number = get_object_or_404(SaleInvoice, pk=self.kwargs['pk'])
        current_obj = SaleInvoiceItem.objects.filter(si_number=line_item.si_number).order_by('-so_line_number').first()
        if current_obj !=None:
            new_line_number = (current_obj.si_line_number) + 1
        else:
            new_line_number = 1
        line_item.si_line_number = new_line_number
        line_item.total_price = line_item.sale_price*line_item.so_quantity
        line_item.so_item_tax_amount = line_item.so_tax_rate.tax_value*line_item.total_price
        line_item.save()
        line_item.so_number.CalculateSoTotal()
        return super().form_valid(form)

class SaleOrderList(ListView):
    model = SaleOrder
    form_class = SaleOrderForm
    template_name = 'salesApp/saleorderlist.html'
    def get_context_data(self, *args, **kwargs):
        so_list = SaleOrder.objects.all()
        for sale_order in so_list:
            sale_order.CalculateSoTotal()
        context = super().get_context_data(*args,**kwargs)
        return context

class ViewInvoices(FormView):
    form_class = InvoiceSearchForm
    template_name = 'salesApp/viewinvoices.html'
    success_url = 'salesApp:viewinvoices'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['object_list'] = SaleInvoice.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        form = ViewInvoiceForm(request.POST)
        if form.is_valid():
            customer_id = form.cleaned_data['customer'].id
            project_id = form.cleaned_data['project'].id
            print(cust_id)
        else:
            context['invalid_search'] = "invalid"
        return self.render_to_response(context)
    #
    #
    # def form_valid(self,form):
    #     print(form.cleaned_data['si_number'])
    #     print(form.cleaned_data['customer'].id)
    #     self.si_number=form.cleaned_data['si_number']
    #     print()
    #     return super().form_valid(form)

    # def get_success_url(self):
#AJAX Calls
def ViewInvoiceList(request):
    # if request.GET.get('customer')
    customer = request.GET.get('customer')
    print("in django view!")
    print(customer)
    result = SaleInvoice.objects.all()
    new_html_table = render_to_string('salesapp/tables/viewinvoicestable.html',{'object_list':result})
    return HttpResponse(new_html_table)
