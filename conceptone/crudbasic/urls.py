from django.urls import path
from crudbasic import views

app_name = 'crudbasic'

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('customers/',views.BaseDisplayView.as_view(),name='customers'),
    path('suppliers/',views.BaseDisplayView.as_view(),name='suppliers'),
    path('projects/',views.BaseDisplayView.as_view(),name='projects'),
    path('items/',views.BaseDisplayView.as_view(),name='items'),
    path('createcustomer/',views.CreateCustomer,name='createcustomer'),
    path('createsupplier/',views.CreateSupplier,name='createsupplier'),
    path('createitem/',views.CreateItem,name='createitem'),
    path('createproject/',views.CreateProject,name='createproject'),
    path('basedisplay/',views.BaseDisplayView.as_view(),name='basedisplay'),
]
