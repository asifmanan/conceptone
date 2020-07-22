from django.urls import path
from saleordersApp import views

app_name = 'saleordersApp'

urlpatterns=[
    path('createsaleorder/',views.CreateSaleOrder.as_view(),name='CreateSaleOrder'),
    path('createsaleorderitem/<int:pk>',views.CreateSaleOrderItem.as_view(),name='CreateSaleOrderItem'),
    path('deletesaleorderitem/delete/<int:pk>',views.DeleteSaleOrderItem.as_view(),name='DeleteSaleOrderItem'),
    path('listsaleorder/',views.ListSaleOrder.as_view(),name='ListSaleOrder'),
    #ajax
    path('saleorderquery/',views.SaleOrderQuery,name='SaleOrderQuery'),
]
