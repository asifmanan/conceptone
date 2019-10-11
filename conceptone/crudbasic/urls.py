from django.urls import path
from crudbasic import views

app_name = 'crudbasic'

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('customers/',views.CustomerView.as_view(),name='customers'),
    path('suppliers/',views.SupplierView.as_view(),name='suppliers'),
    path('items/',views.ItemView.as_view(),name='items'),
    path('projects/',views.ProjectView.as_view(),name='projects'),

    path('createcustomer/',views.CreateCustomerView.as_view(),name='createcustomer'),
    path('createsupplier/',views.CreateSupplierView.as_view(),name='createsupplier'),
    path('createitem/',views.CreateItemView.as_view(),name='createitem'),
    path('createproject/',views.CreateProjectView.as_view(),name='createproject'),

    path('customers/update/<int:pk>/',views.UpdateCustomerView.as_view(),name='updatecustomer'),
    path('suppliers/update/<int:pk>/',views.UpdateSupplierView.as_view(),name='updatesupplier'),
    path('items/update/<int:pk>/',views.UpdateItemView.as_view(),name='updateitem'),
    path('projects/update/<int:pk>/',views.UpdateProjectView.as_view(),name='updateproject'),

    path('customers/delete/<int:pk>',views.DeleteCustomerView.as_view(),name='customerdelete'),
]
