from django.urls import path
from baseApp import views

app_name = 'baseApp'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
]
