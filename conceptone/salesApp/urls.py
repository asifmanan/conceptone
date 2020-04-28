from django.urls import path
from salesApp import views

app_name = 'salesApp'

urlpatterns=[
    path('createinvoice/',views.CreateInvoice.as_view(),name='createinvoice'),
    path('createsaleorder/',views.CreateSaleOrder.as_view(),name='createsaleorder'),
    path('addsaleorderitem/<int:pk>/',views.AddSaleOrderItems.as_view(),name='addsaleorderitems'),
    path('saleorderlist/',views.SaleOrderList.as_view(),name='saleorderlist'),
]
