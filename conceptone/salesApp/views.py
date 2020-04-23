from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.http import FileResponse
from salesApp.models import SaleOrder, SaleInvoice
from salesApp.forms import SaleInvoiceForm, SaleOrderForm
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
