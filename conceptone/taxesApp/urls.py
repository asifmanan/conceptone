from django.urls import path
from taxesApp import views

app_name = 'taxesApp'

urlpatterns=[
    path('createtax/',views.CreateTax.as_view(),name='CreateTax'),
    path('createtaxauthority/',views.CreateTaxAuthority.as_view(),name='CreateTaxAuthority'),
    path('listtaxes/',views.ListTaxes.as_view(),name='ListTaxes'),
    path('listtaxauthorities/',views.ListTaxAuthorities.as_view(),name='ListTaxAuthorities'),
]
