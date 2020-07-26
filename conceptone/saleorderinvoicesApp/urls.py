from django.urls import path
from saleorderinvoicesApp import views

app_name = 'saleorderinvoicesApp'

urlpatterns=[
    path('createsaleorderinvoice/',views.CreateSaleOrderInvoice.as_view(),name='CreateSaleOrderInvoice'),
    #AJAX
    path('ajaxcall/getformdata/',views.GetFormData,name='GetFormData'),
]
