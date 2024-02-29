from django.db import models
from django.utils import timezone
from customersApp.models import Customer
from baseApp.models import Company
# Create your models here.
class Project(models.Model):
    status_flags = [
        ('Completed','Completed'),
        ('On-Going','On-Going'),
        ('Delivered','Delivered'),
    ]
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    project_code = models.CharField(max_length=16, unique=True)
    project_name = models.CharField(max_length=128, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    project_status = models.CharField(max_length=16,choices=status_flags)
    contract_number = models.CharField(max_length=128, unique=True)
    contract_signing_date = models.DateField()
    award_date = models.DateField()
    delivery_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name

    def this_class_name(self):
        return 'Project'
