from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
    customer_code = models.CharField(max_length=16, unique=True)
    customer_name = models.CharField(max_length=128, unique=True)
    customer_address = models.CharField(max_length=264)
    customer_city = models.CharField(max_length=128)
    customer_phone = models.CharField(max_length=128, blank=True)
    customer_fax = models.CharField(max_length=128, blank=True)
    customer_email = models.EmailField(max_length=192, blank=True)
    customer_ntn_number = models.CharField(max_length=128, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_name

    def this_class_name(self):
        return 'Customer'
