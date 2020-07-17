from django.urls import path
from standardinvoiceApp import views

app_name = 'standardinvoiceApp'

urlpatterns = [
    path('createstandardinvoice/',views.CreateStandardInvoice.as_view(),name='CreateStandardInvoice'),
    path('createstandardinvoiceitem/<int:pk>',views.CreateStandardInvoiceItem.as_view(),name='CreateStandardInvoiceItem'),
    path('deletestandardinvoiceitem/delete/<int:pk>',views.DeleteStandardInvoiceItem.as_view(),name='DeleteStandardInvoiceItem'),
]
