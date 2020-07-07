from django.urls import path
from projectsApp import views

app_name = 'projectsApp'

urlpatterns = [
    path('createproject/',views.CreateProject.as_view(),name='CreateProject'),
    path('listprojects/',views.ListProjects.as_view(),name='ListProjects'),
]
