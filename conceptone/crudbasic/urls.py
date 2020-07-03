from django.urls import path
from crudbasic import views

app_name = 'crudbasic'

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('projects/',views.ProjectView.as_view(),name='projects'),
    path('taxrates/',views.TaxRateView.as_view(),name='taxrates'),

    path('createproject/',views.CreateProjectView.as_view(),name='createproject'),
    path('createtax/',views.CreateTaxRateView.as_view(),name='createtax'),

    path('projects/update/<int:pk>/',views.UpdateProjectView.as_view(),name='updateproject'),
    path('taxrates/update/<int:pk>/',views.UpdateTaxRateView.as_view(),name='updatetaxrate'),

    path('projects/delete/<int:pk>',views.DeleteProjectView.as_view(),name='projectdelete'),
    path('taxrates/delete/<int:pk>',views.DeleteTaxRateView.as_view(),name='taxratedelete'),
    # path('purchaseorders/delete/<int:pk>',views.DeletePurchaseOrderView.as_view(),name='purchaseorderdelete'),

    # path('purchaseorders/publish/<int:pk>',views.PoPublishConfirmation,name='publishpo'),
    # path('ajax/loaditemrates/', views.loaditemrates, name='loaditemrates'),

]
