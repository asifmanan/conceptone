from django.urls import path
from itemsApp import views

app_name = 'itemsApp'

urlpatterns = [
    path('createitem/',views.CreateItem.as_view(),name='CreateItem'),
    path('listitems/',views.ListItems.as_view(),name='ListItems'),
    # ajax
    path('itemquery',views.ItemQuery,name='ItemQuery')
]
