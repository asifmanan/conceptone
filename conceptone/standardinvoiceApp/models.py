from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.db.models import Sum
from baseApp.models import Company
from customersApp.models import Customer
from projectsApp.models import Project
from taxesApp.models import Tax
from itemsApp.models import Item
# Create your models here.
class StandardInvoice(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    project = models.ForeignKey(Project,on_delete=models.PROTECT)
    invoice_number = models.CharField(unique=True,max_length=56)
    invoice_date = models.DateField()
    amount_exclusive_tax = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    tax_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    total_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def CalculateInvoiceTotal(self):
        items = StandardInvoiceItem.objects.filter(invoice=self)
        if items.exists():
            items_sum = items.aggregate(Sum('total_price'))
            invoice_items_sum = items_sum['total_price__sum']
            items_tax = items.aggregate(Sum('tax_amount'))
            invoice_items_tax_sum = items_tax['tax_amount__sum']
            total_amount = invoice_items_sum+invoice_items_tax_sum
            self.amount_exclusive_tax = invoice_items_sum
            self.tax_amount = invoice_items_tax_sum
            self.total_amount = total_amount
            self.save()

    def __str__(self):
        return self.invoice_number

class StandardInvoiceItem(models.Model):
    invoice = models.ForeignKey(StandardInvoice, on_delete=models.CASCADE)
    line_number = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    tax = models.ForeignKey(Tax,on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=14,decimal_places=2)
    sale_price = models.DecimalField(max_digits=14,decimal_places=2)
    total_price = models.DecimalField(max_digits=14,decimal_places=2)
    tax_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    total_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def add_amount_to_invoice(self):
        self.invoice.amount_exclusive_tax += self.total_price
        self.invoice.tax_amount += self.tax_amount
        self.invoice.total_amount += self.total_price+self.tax_amount
        self.invoice.save()

    def remove_amount_from_invoice(self):
        self.invoice.amount_exclusive_tax -= self.total_price
        self.invoice.tax_amount -= self.tax_amount
        self.invoice.total_amount -= self.total_price+self.tax_amount
        self.invoice.save()

    def __str__(self):
        return self.item
