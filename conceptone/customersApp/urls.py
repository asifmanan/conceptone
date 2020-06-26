from django.urls import path
from customersApp import views

app_name = 'customersApp'

urlpatterns = [
    path('createcustomer/',views.CreateCustomer.as_view(),name='CreateCustomer'),
    path('listcustomers/',views.ListCustomers.as_view(),name='ListCustomers'),
    #ajax
    path('customerquery/',views.CustomerQuery,name='CustomerQuery')
]
