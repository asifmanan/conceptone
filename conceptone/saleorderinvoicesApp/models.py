from django.db import models
from django.utils import timezone
from saleordersApp.models import SaleOrder, SaleOrderItem
from baseApp.models import Company

# Create your models here.

class SaleOrderInvoice(models.Model):
    supplier = models.ForeignKey(Company, on_delete=models.PROTECT, blank=True)
    sale_order = models.ForeignKey(SaleOrder, on_delete=models.PROTECT)
    invoice_number = models.CharField(max_length=56)
    invoice_date = models.DateField()
    amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    tax_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    total_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.invoice_number

class SaleOrderInvoiceItem(models.Model):
    sale_order_invoice = models.ForeignKey(SaleOrderInvoice, on_delete=models.PROTECT)
    item = models.ForeignKey(SaleOrderItem, on_delete=models.PROTECT)
    bill_quantity = models.DecimalField(max_digits=14,decimal_places=4)
    amount = models.DecimalField(max_digits=14,decimal_places=2)
    tax_amount = models.DecimalField(max_digits=14,decimal_places=2)
    total_amount = models.DecimalField(max_digits=14,decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
