from django.urls import path
from purchaseApp import views

app_name = 'purchaseApp'

urlpatterns=[
    path('createpurchaseorder/',views.CreatePurchaseOrder.as_view(),name='createpurchaseorder'),
]
