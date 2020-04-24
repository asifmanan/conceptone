from django.shortcuts import render
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

class CreateInvoice(CreateView):
    model = SaleInvoice
    form_class = SaleInvoiceForm
    template_name = 'salesApp/createinvoice.html'

class AddSaleOrderItems(CreateView):
    model = SaleOrderItem
    form_class = SaleOrderItemForm
    template_name = 'salesApp/soadditem.html'
    def get_context_data():
        context = super().get_context_data(*args,**kwargs)
        context['so'] = SaleOrder.objects.filter(pk=self.args.get('pk'))
        return context
