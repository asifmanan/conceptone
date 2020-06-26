from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Company(models.Model):
    company_code = models.CharField(max_length=16, unique=True)
    company_name = models.CharField(max_length=128)
    company_address = models.CharField(max_length=264)
    company_ntn_number = models.CharField(max_length=128)
    company_city = models.CharField(max_length=128)
    company_phone = models.CharField(max_length=128)
    company_fax = models.CharField(max_length=128, blank=True)
    company_email = models.EmailField(max_length=192)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
