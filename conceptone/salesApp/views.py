from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.http import FileResponse
from . import models
from django.views.generic import View, TemplateView, ListView, DetailView,
                                    CreateView, UpdateView, DetailView
# Create your views here.
class SaleOrderListView(ListView):
    model = SaleOrder
    
