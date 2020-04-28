from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.http import FileResponse
from salesApp.models import SaleOrder, SaleInvoice, SaleOrderItem
from salesApp.forms import SaleInvoiceForm, SaleOrderForm, SaleOrderItemForm
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                    CreateView, UpdateView, DetailView)
# Create your views here.
class CreateSaleOrder(CreateView):
    model = SaleOrder
    form_class = SaleOrderForm
    template_name = 'salesApp/createsaleorder.html'
    def get_success_url(self):
        return reverse_lazy('salesApp:addsaleorderitems',kwargs={'pk':self.object.pk})

class CreateInvoice(CreateView):
    model = SaleInvoice
    form_class = SaleInvoiceForm
    template_name = 'salesApp/createinvoice.html'

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

class SaleOrderList(ListView):
    model = SaleOrder
    form_class = SaleOrderForm
    template_name = 'salesApp/saleorderlist.html'
