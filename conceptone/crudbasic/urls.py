from django.urls import path
from crudbasic import views

app_name = 'crudbasic'

urlpatterns=[
    path('',views.index,name='index'),
    path('customers/',views.customers,name='customers'),
    path('suppliers/',views.suppliers,name='suppliers'),
    path('projects/',views.projects,name='projects'),
    path('items/',views.items,name='items'),
    path('createcustomer/',views.CreateCustomer,name='createcustomer'),
]
