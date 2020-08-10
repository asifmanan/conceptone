from django.urls import path
from saleorderinvoicesApp import views

app_name = 'saleorderinvoicesApp'

urlpatterns=[
    path('newsaleorderinvoice/',views.NewSaleOrderInvoice.as_view(),name='NewSaleOrderInvoice'),

    path('listsaleorderinvoice/',views.ListSaleOrderInvioce.as_view(),name='ListSaleOrderInvoice'),
    # path('createsaleorderinvoiceinitial/',views.CreateSaleOrderInvoiceInitial.as_view(),name='CreateSaleOrderInvoiceInitial'),
    #AJAX
    path('ajaxcall/selectsupplier/',views.SelectSupplier,name='SelectSupplier'),
    path('ajaxcall/selectsaleorder/',views.SelectSaleOrder,name='SelectSaleOrder'),
    path('ajaxcall/selectsaleorderitem/',views.SelectSaleOrderItem,name='SelectSaleOrderItem'),
]
