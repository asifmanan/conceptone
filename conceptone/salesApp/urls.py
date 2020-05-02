from django.urls import path
from salesApp import views

app_name = 'salesApp'

urlpatterns=[
    path('createsoinvoice/',views.CreateSoInvoice.as_view(),name='createsoinvoice'),
    path('createnewinvoice/',views.CreateNewInvoice.as_view(),name='createnewinvoice'),
    path('createsaleorder/',views.CreateSaleOrder.as_view(),name='createsaleorder'),
    path('addsaleorderitem/<int:pk>/',views.AddSaleOrderItems.as_view(),name='addsaleorderitems'),
    path('saleorderlist/',views.SaleOrderList.as_view(),name='saleorderlist'),
    path('addsiitemfromso/<int:pk>',views.AddSaleInvoiceItemsFromSo.as_view(),name='addsiitemfromso'),
]
