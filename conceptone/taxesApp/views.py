from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from taxesApp.models import Tax, TaxAuthority
from taxesApp.forms import TaxForm, TaxAuthorityForm
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, FormView
# Create your views here.
class CreateTax(CreateView):
    model = Tax
    form_class = TaxForm
    template_name = 'taxesapp/create_tax.html'

class CreateTaxAuthority(CreateView):
    model = TaxAuthority
    form_class = TaxAuthorityForm
    template_name = 'taxesapp/create_taxauthority.html'
