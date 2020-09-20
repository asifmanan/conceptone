from django.urls import path
from saleorderinvoicesApp import views

app_name = 'saleorderinvoicesApp'

urlpatterns=[
    path('newsaleorderinvoice/',views.NewSaleOrderInvoice.as_view(),name='NewSaleOrderInvoice'),
    path('createsaleorderinvoiceitem/',views.CreateSaleOrderInvoiceItem.as_view(),name='CreateSaleOrderInvoiceItem'),
    path('listsaleorderinvoice/',views.ListSaleOrderInvioce.as_view(),name='ListSaleOrderInvoice'),
    path('listpublishedsaleorderinvoice/',views.ListPublishedSaleOrderInvoice.as_view(),name='ListPublishedSaleOrderInvoice'),
    path('listunpublishedsaleorderinvoice/',views.ListUnpublishedSaleOrderInvoice.as_view(),name='ListUnpublishedSaleOrderInvoice'),
    path('detailsaleorderinvoice/<int:pk>',views.DetailSaleOrderInvoice.as_view(),name='DetailSaleOrderInvoice'),
    # path('createsaleorderinvoiceinitial/',views.CreateSaleOrderInvoiceInitial.as_view(),name='CreateSaleOrderInvoiceInitial'),
    # Function views:
    path('cancelnewsaleorderinvoice/',views.CancelNewSaleOrderInvoiceSession,name='CancelNewSaleOrderInvoiceSession'),
    path('publishsaleorderinvoice/<int:pk>',views.PublishSaleOrderInvoice.as_view(),name='PublishSaleOrderInvoice'),
    #AJAX
    path('ajaxcall/selectsupplier/',views.SelectSupplier,name='SelectSupplier'),
    path('ajaxcall/selectsaleorder/',views.SelectSaleOrder,name='SelectSaleOrder'),
    path('ajaxcall/selectsaleorderitem/',views.SelectSaleOrderItem,name='SelectSaleOrderItem'),
]
