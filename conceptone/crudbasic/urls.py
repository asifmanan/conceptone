from django.urls import path
from crudbasic import views

app_name = 'crudbasic'

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('items/',views.ItemView.as_view(),name='items'),
    path('projects/',views.ProjectView.as_view(),name='projects'),
    path('taxrates/',views.TaxRateView.as_view(),name='taxrates'),

    path('createitem/',views.CreateItemView.as_view(),name='createitem'),
    path('createproject/',views.CreateProjectView.as_view(),name='createproject'),
    path('createtax/',views.CreateTaxRateView.as_view(),name='createtax'),

    path('items/update/<int:pk>/',views.UpdateItemView.as_view(),name='updateitem'),
    path('projects/update/<int:pk>/',views.UpdateProjectView.as_view(),name='updateproject'),
    path('taxrates/update/<int:pk>/',views.UpdateTaxRateView.as_view(),name='updatetaxrate'),

    path('items/delete/<int:pk>',views.DeleteItemView.as_view(),name='itemdelete'),
    path('projects/delete/<int:pk>',views.DeleteProjectView.as_view(),name='projectdelete'),
    path('taxrates/delete/<int:pk>',views.DeleteTaxRateView.as_view(),name='taxratedelete'),
    # path('purchaseorders/delete/<int:pk>',views.DeletePurchaseOrderView.as_view(),name='purchaseorderdelete'),

    # path('purchaseorders/publish/<int:pk>',views.PoPublishConfirmation,name='publishpo'),
    # path('ajax/loaditemrates/', views.loaditemrates, name='loaditemrates'),

]
