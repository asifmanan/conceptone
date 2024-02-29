from django.urls import path
from suppliersApp import views

app_name = 'suppliersApp'

urlpatterns=[
    path('createsupplier/',views.CreateSupplier.as_view(),name='CreateSupplier'),
    path('listsuppliers/',views.ListSuppliers.as_view(),name='ListSuppliers'),
    #AJAX
    path('supplierquery/',views.SupplierQuery,name='SupplierQuery'),
]
