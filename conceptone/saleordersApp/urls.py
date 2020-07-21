from django.urls import path
from saleordersApp import views

app_name = 'saleordersApp'

urlpatterns=[
    path('createsaleorder/',views.CreateSaleOrder.as_view(),name='CreateSaleOrder'),
]
