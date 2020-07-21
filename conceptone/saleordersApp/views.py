from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from django.views.generic import (
                                CreateView,
                                )

from saleordersApp.models import SaleOrder, SaleOrderItem
from saleordersApp.forms import (
                                SaleOrderForm,
                                SaleOrderItemForm,
                                )
# Create your views here.
class CreateSaleOrder(CreateView):
    model = SaleOrder
    form_class = SaleOrderForm
    template_name = 'saleordersapp/create_saleorder.html'
