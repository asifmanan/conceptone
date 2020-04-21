from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models import Sum
from crudbasic.models import Customers, Items, TaxRate

# Create your models here.
class SaleOrder(models.Model):
    so_number = models.CharField(max_length=24)
    so_date = models.DateField()
    so_customer = models.ForeignKey(Customers, on_delete=models.PROTECT)
    so_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    so_tax = models.ForeignKey(TaxRate, on_delete=models.PROTECT)
    so_tax_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    so_draft = models.BooleanField(default=True)
    so_publish = models.BooleanField(default=False)
    so_publish_date = models.DateTimeField(blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def publish(self):
        self.so_publish_date = timezone.now()
        self.so_publish = True
        self.save()

    def CalculateSoTotal(self):
        pass

    def __str__(self):
        return self.so_number

class SaleOrderItem(models.Model):
    so_line_number = models.IntegerField(verbose_name='Line')
    sale_order_item = models.ForeignKey(Items, on_delete=models.PROTECT,verbose_name='Item')
    so_number = models.ForeignKey(SaleOrder, on_delete=models.CASCADE)
    so_quantity = models.DecimalField(max_digits=14,decimal_places=2,default=0.00,verbose_name='Quantity')
    sale_price = models.DecimalField(max_digits=14,decimal_places=2,verbose_name='Sale Price')
    total_price = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    variation_number = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.po_line_number)
