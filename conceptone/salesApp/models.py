from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models import Sum
from crudbasic.models import Customers, Items, TaxRate, Projects

# Create your models here.
class SaleOrder(models.Model):
    so_number = models.CharField(max_length=24,verbose_name='SO Number')
    so_ponumber = models.CharField(max_length=48,verbose_name='PO Number')
    so_customer = models.ForeignKey(Customers, on_delete=models.PROTECT,verbose_name='Customer')
    so_project = models.ForeignKey(Projects, on_delete=models.PROTECT,verbose_name='Project')
    so_podate = models.DateField(verbose_name='PO Date', null=True)
    so_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
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
        items = SaleOrderItem.objects.filter(so_number=self)
        if items.exists():
            items_sum = items.aggregate(Sum('total_price'))
            items_tax = items.aggregate(Sum('so_item_tax_amount'))
            items_total_amount = items_sum['total_price__sum']
            items_total_tax_amount = items_tax['so_item_tax_amount__sum']
            self.so_amount = items_total_amount
            self.so_tax_amount = items_total_tax_amount
            self.save()

    def __str__(self):
        return self.so_number

    def get_absolute_url(self):
        return reverse('salesApp:addsaleorderitems',kwargs={'pk':self.pk})

class SaleOrderItem(models.Model):
    so_line_number = models.IntegerField(verbose_name='Line')
    sale_order_item = models.ForeignKey(Items, on_delete=models.PROTECT,verbose_name='Item')
    so_number = models.ForeignKey(SaleOrder, on_delete=models.CASCADE)
    so_quantity = models.DecimalField(max_digits=14,decimal_places=2,default=0.00,verbose_name='Quantity')
    sale_price = models.DecimalField(max_digits=14,decimal_places=2,verbose_name='Sale Price')
    so_tax_rate = models.ForeignKey(TaxRate, on_delete=models.PROTECT)
    so_item_tax_amount = models.DecimalField(max_digits=14,decimal_places=2,verbose_name='Tax Amount')
    total_price = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    variation_number = models.IntegerField(default=0)
    variation_quantity = models.DecimalField(max_digits=14,decimal_places=2,default=0,verbose_name='Variation Quantity')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.so_line_number)

class SaleInvoice(models.Model):
    si_sonumber = models.ForeignKey(SaleOrder,on_delete=models.PROTECT,verbose_name='SO Number',null=True)
    si_number = models.CharField(max_length=24,verbose_name='Invoice Number')
    si_customer = models.ForeignKey(Customers,on_delete=models.PROTECT,verbose_name='Customer')
    si_project = models.ForeignKey(Projects,on_delete=models.PROTECT,verbose_name='Project')
    si_tax_amount = models.DecimalField(max_digits=14,decimal_places=2,verbose_name='Tax Amount')
    si_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00, verbose_name='Grand Total')
    si_date = models.DateField(verbose_name='Invoice Date')

class SaleInvoiceItems(models.Model):
    si_number = models.ForeignKey(SaleInvoice, on_delete=models.CASCADE)
    si_item = models.ForeignKey(SaleOrderItem, on_delete=models.CASCADE)
    si_item_bill_quantity = models.DecimalField(max_digits=14,decimal_places=2,default=0.00,verbose_name='Quantity')
    si_item_tax_rate = models.ForeignKey(TaxRate, on_delete=models.PROTECT)
    si_item_tax_amount = models.DecimalField(max_digits=14,decimal_places=2,verbose_name='Tax Amount')
    si_item_total_amount = models.DecimalField(max_digits=14,decimal_places=2,verbose_name='Total Amount')
