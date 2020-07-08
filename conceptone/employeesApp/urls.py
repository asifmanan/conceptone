from django.urls import path
from employeesApp import views

app_name = 'employeesApp'

urlpatterns = [
    path('createemployee/',views.CreateEmployee.as_view(),name='CreateEmployee'),
    path('listemployees/',views.ListEmployees.as_view(),name='ListEmployees'),
]
