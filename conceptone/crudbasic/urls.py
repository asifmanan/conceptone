from django.urls import path
from crudbasic import views

app_name = 'crudbasic'

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('customers/',views.CustomerView.as_view(),name='customers'),
    path('suppliers/',views.SupplierView.as_view(),name='suppliers'),
    path('items/',views.ItemView.as_view(),name='items'),
    path('projects/',views.ProjectView.as_view(),name='projects'),
    path('taxrates/',views.TaxRateView.as_view(),name='taxrates'),
    path('purchaseorders/',views.PurchaseOrderView.as_view(),name='purchaseorders'),

    path('createcustomer/',views.CreateCustomerView.as_view(),name='createcustomer'),
    path('createsupplier/',views.CreateSupplierView.as_view(),name='createsupplier'),
    path('createitem/',views.CreateItemView.as_view(),name='createitem'),
    path('createproject/',views.CreateProjectView.as_view(),name='createproject'),
    path('createtax/',views.CreateTaxRateView.as_view(),name='createtax'),
    path('newpurchaseorder/',views.CreatePurchaseOrder.as_view(),name='newpurchaseorder'),
    path('neworderitems/<int:pk>',views.CreateOrderItem,name='neworderitems'),

    path('customers/update/<int:pk>/',views.UpdateCustomerView.as_view(),name='updatecustomer'),
    path('suppliers/update/<int:pk>/',views.UpdateSupplierView.as_view(),name='updatesupplier'),
    path('items/update/<int:pk>/',views.UpdateItemView.as_view(),name='updateitem'),
    path('projects/update/<int:pk>/',views.UpdateProjectView.as_view(),name='updateproject'),
    path('taxrates/update/<int:pk>/',views.UpdateTaxRateView.as_view(),name='updatetaxrate'),
    path('purchaseorders/update/<int:pk>/',views.UpdatePurchaseOrder.as_view(),name='updatepurchaseorder'),

    path('customers/delete/<int:pk>',views.DeleteCustomerView.as_view(),name='customerdelete'),
    path('suppliers/delete/<int:pk>',views.DeleteSupplierView.as_view(),name='supplierdelete'),
    path('items/delete/<int:pk>',views.DeleteItemView.as_view(),name='itemdelete'),
    path('projects/delete/<int:pk>',views.DeleteProjectView.as_view(),name='projectdelete'),
    path('taxrates/delete/<int:pk>',views.DeleteTaxRateView.as_view(),name='taxratedelete'),
]
