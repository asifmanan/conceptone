from django.urls import path
from standardinvoiceApp import views

app_name = 'standardinvoiceApp'

urlpatterns = [
    path('createstandardinvoice/',views.CreateStandardInvoice.as_view(),name='CreateStandardInvoice'),
]
