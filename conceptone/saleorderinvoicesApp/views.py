from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.views.generic import (
                                CreateView,
                                DeleteView,
                                FormView,
                                )
from saleorderinvoicesApp.models import (
                                        SaleOrderInvoice,
                                        SaleOrderInvoiceItem,
                                        )
from saleorderinvoicesApp.forms import (
                                        SaleOrderInvoiceForm,
                                        )
# Create your views here.
class CreateSaleOrderInvoice(CreateView):
    model = SaleOrderInvoice
    form_class = SaleOrderInvoiceForm
    template_name = 'saleorderinvoiceapp/create_saleorderinvoice.html'
    
