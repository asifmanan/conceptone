from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.http import FileResponse
from salesApp.models import SaleOrder, SaleInvoice, SaleOrderItem, SaleInvoiceItem
from salesApp.forms import SaleInvoiceSoForm, SaleInvoiceNewForm, SaleOrderForm, SaleOrderItemForm, SaleInvoiceItemForm, SelectItemFromSo, InputInvoiceItemQuantity
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
        self.so = form.cleaned_data['si_sonumber']
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
        context['so'] = get_object_or_404(SaleOrder, pk=self.kwargs['pk'])
        so_items = SaleOrderItem.objects.filter(so_number=self.kwargs['pk'])
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
        else:
            request.session['invoice-selected_item'] = selected_items
        print("*** After POST ***")
        issubset = set(selected_items) <= set(context['item_list'])
        print(issubset)
        print(selected_items)
        print(context['item_list'])
        return redirect('salesApp:createinvoiceso') #Just a test

class CreateInvoiceSo(CreateView):
    model = SaleInvoiceItem
    form_class = InputInvoiceItemQuantity
    template_name = 'salesApp/createsoinvoiceitems.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        selected_items = self.request.session['invoice-selected_item']
        invoice_items = SaleOrderItem.objects.filter(id__in=selected_items)
        print('in the new view')
        print(invoice_items)
        print(selected_items)

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
        context['items'] = SaleOrderItem.objects.filter(so_number=self.kwargs['pk'])
        return context
    def form_valid(self,form):
        line_item = form.save(commit=False)
        line_item.so_number = get_object_or_404(SaleOrder, pk=self.kwargs['pk'])
        current_obj = SaleOrderItem.objects.filter(so_number=line_item.so_number).order_by('-so_line_number').first()
        if current_obj !=None:
            new_line_number = (current_obj.so_line_number) + 1
        else:
            new_line_number = 1
        line_item.so_line_number = new_line_number
        line_item.total_price = line_item.sale_price*line_item.so_quantity
        line_item.so_item_tax_amount = line_item.so_tax_rate.tax_value*line_item.total_price
        line_item.save()
        line_item.so_number.CalculateSoTotal()
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('salesApp:addsaleorderitems',kwargs={'pk':self.object.so_number.pk})

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
