from django.urls import path
from crudbasic import views

app_name = 'crudbasic'

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('customers/',views.CustomerView.as_view(),name='customers'),
    path('suppliers/',views.suppliers,name='suppliers'),
    path('projects/',views.projects,name='projects'),
    path('items/',views.items,name='items'),
    path('createcustomer/',views.CreateCustomer,name='createcustomer'),
    path('createsupplier/',views.CreateSupplier,name='createsupplier'),
    path('createitem/',views.CreateItem,name='createitem'),
    path('createproject/',views.CreateProject,name='createproject'),
]
