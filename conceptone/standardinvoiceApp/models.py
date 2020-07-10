from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from customersApp.models import Customer
from projectsApp.models import Project
from taxesApp.models import Tax
from itemsApp.models import Item
# Create your models here.
class StandardInvoice(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    project = models.ForeignKey(Project,on_delete=models.PROTECT)
    invoice_number = models.CharField(unique=True,max_length=56)
    invoice_date = models.DateField()
    amount_exclusive_tax = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    tax_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    total_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.invoice_number

class StandardInvoiceItem(models.Model):
    invoice = models.ForeignKey(StandardInvoice, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    tax = models.ForeignKey(Tax,on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    sale_price = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    total_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    tax_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item
