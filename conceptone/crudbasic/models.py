from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models import Sum
from customersApp.models import Customer

# Create your models here.

class Projects(models.Model):
    status_flags = [
        ('Prospective','Prospective'),
        ('Completed','Completed'),
        ('On-Going','On-Going'),
    ]
    project_code = models.CharField(max_length=16, unique=True)
    project_name = models.CharField(max_length=128, unique=True)
    project_customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    project_city = models.CharField(max_length=128)
    project_status = models.CharField(max_length=16,choices=status_flags)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name

    def this_class_name(self):
        return 'Project'

class TaxRate(models.Model):
    tax_jurisdiction_choices = [
    ('KP','Khyber Pakhtunkhwa'),
    ('Punjab', 'Punjab'),
    ('Baluchistan','Baluchistan'),
    ('Sindh','Sindh'),
    ('Federal','Federal'),
    ]
    tax_code = models.CharField(max_length=16)
    tax_name = models.CharField(max_length=64)
    tax_jurisdiction = models.CharField(max_length=64,choices=tax_jurisdiction_choices)
    tax_value = models.DecimalField(max_digits=5, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tax_name

# class AccountsTable(models.Model):
