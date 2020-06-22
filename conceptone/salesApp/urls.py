from django.urls import path
from salesApp import views

app_name = 'salesApp'

urlpatterns=[
    path('createsaleorder/',views.CreateSaleOrder.as_view(),name='createsaleorder'),
    path('addsaleorderitem/<int:pk>',views.AddSaleOrderItems.as_view(),name='addsaleorderitems'),
    path('listsaleorders/',views.ListSaleOrders.as_view(),name='ListSaleOrders'),
    path('createsoinvoice/',views.CreateSoInvoice.as_view(),name='createsoinvoice'),
    path('selectsiitemfromso/<int:pk>',views.SelectSaleInvoiceItemsFromSo.as_view(),name='selectsiitemfromso'),
    path('createinvoiceso/',views.CreateInvoiceSo.as_view(),name='createinvoiceso'),
    path('viewinvoices/',views.ViewInvoices.as_view(),name='viewinvoices'),
    #AJAX Views
    path('viewinvoicelist/',views.ViewInvoiceList,name='viewinvoicelist'),
    path('saleorderquery/',views.SaleOrderQuery,name='SaleOrderQuery'),
]
