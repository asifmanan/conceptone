from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
# Create your views here.
class IndexView(TemplateView):
    template_name = 'baseApp/index.html'
