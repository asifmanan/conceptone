from django.urls import path
from purchaseApp import views

app_name = 'purchaseApp'

urlpatterns=[
    path('createpurchaseorder/',views.CreatePurchaseOrder.as_view(),name='createpurchaseorder'),
    path('createpurchaseorderitems/<int:pk>',views.CreatePurchaseOrderItems.as_view(),name='CreatePurchaseOrderItems'),
    path('listpurchaseorders/',views.ListPurchaseOrders.as_view(),name='ListPurchaseOrders'),
    #ajax
    path('purchaseorderquery/',views.PurchaseOrderQuery,name='PurchaseOrderQuery'),

    path('purchaseorder/delete/<int:pk>',views.DeletePurchaseOrder.as_view(),name='DeletePurchaseOrder'),
    path('purchaseorderitem/delete/<int:pk>',views.DeletePurchaseOrderItem.as_view(),name='DeletePurchaseOrderItem')
]
