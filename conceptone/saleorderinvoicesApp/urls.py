from django.urls import path
from saleorderinvoicesApp import views

app_name = 'saleorderinvoicesApp'

urlpatterns=[
    path('createsaleorderinvoice/',views.CreateSaleOrderInvoice.as_view(),name='CreateSaleOrderInvoice'),
    path('listsaleorderinvoice/',views.ListSaleOrderInvioce.as_view(),name='ListSaleOrderInvoice'),
    path('createsaleorderinvoiceinitial/',views.CreateSaleOrderInvoiceInitial.as_view(),name='CreateSaleOrderInvoiceInitial'),
    #AJAX
    path('ajaxcall/getformdata/',views.GetFormData,name='GetFormData'),
]
