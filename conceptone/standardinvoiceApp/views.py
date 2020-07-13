from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, FormView

from standardinvoiceApp.models import StandardInvoice, StandardInvoiceItem
from standardinvoiceApp.forms import StandardInvoiceForm
# Create your views here.
class CreateStandardInvoice(CreateView):
    model = StandardInvoice
    form_class = StandardInvoiceForm
    template_name = 'standardinvoiceapp/create_standardinvoice.html'