from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models import Sum
from crudbasic.models import Projects
from taxesApp.models import Tax
from itemsApp.models import Item
from customersApp.models import Customer

# Create your models here.
class SaleOrder(models.Model):
    so_number = models.CharField(max_length=24,verbose_name='SO Number')
    customer_po_number = models.CharField(max_length=48,verbose_name='PO Number')
    customer_po_date = models.DateField(verbose_name='PO Date', null=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT,verbose_name='Customer')
    project = models.ForeignKey(Projects, on_delete=models.PROTECT,verbose_name='Project')
    so_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    tax_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    total_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00,verbose_name='Total Amount')
    is_draft = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)
    publish_date = models.DateTimeField(blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def publish(self):
        self.is_published = True
        self.publish_date = timezone.now()
        self.save()

    def CalculateSoTotal(self):
        items = SaleOrderItem.objects.filter(sale_order=self)
        if items.exists():
            items_sum = items.aggregate(Sum('total_price'))
            items_tax = items.aggregate(Sum('tax_amount'))
            items_total_amount = items_sum['total_price__sum']
            items_total_tax_amount = items_tax['tax_amount__sum']
            self.so_amount = items_total_amount
            self.tax_amount = items_total_tax_amount
            self.total_amount = items_total_amount + items_total_tax_amount
            self.save()

    def __str__(self):
        return self.so_number

    def get_absolute_url(self):
        return reverse('salesApp:addsaleorderitems',kwargs={'pk':self.pk})

class SaleOrderItem(models.Model):
    so_line_number = models.IntegerField(verbose_name='Line')
    item = models.ForeignKey(Item, on_delete=models.PROTECT,verbose_name='Item')
    sale_order = models.ForeignKey(SaleOrder, on_delete=models.CASCADE)
    order_quantity = models.DecimalField(max_digits=14,decimal_places=2,default=0.00,verbose_name='Order Quantity')
    available_quantity = models.DecimalField(max_digits=14,decimal_places=2,default=0.00,verbose_name='Available Quantity')
    billed_quantity = models.DecimalField(max_digits=14,decimal_places=2,default=0.00,verbose_name='Billed Quantity')
    unit_price = models.DecimalField(max_digits=14,decimal_places=2,verbose_name='Sale Price')
    total_price = models.DecimalField(max_digits=14,decimal_places=2,default=0.00,verbose_name='Total Price')
    tax_rate = models.ForeignKey(Tax, on_delete=models.PROTECT)
    tax_amount = models.DecimalField(max_digits=14,decimal_places=2,verbose_name='Tax Amount')
    total_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    variation_number = models.IntegerField(default=0)
    variation_quantity = models.DecimalField(max_digits=14,decimal_places=2,default=0,verbose_name='Variation Quantity')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def ConsumeQuantity(self,invoice_quantity):
        if invoice_quantity <= self.available_quantity:
            self.billed_quantity += invoice_quantity
            self.available_quantity -= invoice_quantity
            self.save()

    def __str__(self):
        return str(self.so_line_number)

class SaleInvoice(models.Model):
    sale_order = models.ForeignKey(SaleOrder,on_delete=models.PROTECT,verbose_name='SO Number',null=True)
    # si_sonumber -> sale_order
    si_number = models.CharField(max_length=24,verbose_name='Invoice Number',null=True)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT,verbose_name='Customer',null=True)
    # si_customer
    project = models.ForeignKey(Projects,on_delete=models.PROTECT,verbose_name='Project',null=True)
    # si_project
    tax_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00, verbose_name='Tax Amount')
    # si_tax_amount
    si_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00, verbose_name='Grand Total')
    si_date = models.DateField(verbose_name='Invoice Date')
    is_published = models.BooleanField(default=False)
    publish_date = models.DateTimeField(blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def publish(self):
        self.is_published = True
        self.publish_date = timezone.now()
        self.save()

    def CalculateSiTotal(self):
        items = SaleInvoiceItem.objects.filter(sale_invoice=self)
        if items.exists():
            items_sum = items.aggregate(Sum('total_price'))
            items_tax = items.aggregate(Sum('tax_amount'))
            items_total_amount = items_sum['total_price__sum']
            items_total_tax_amount = items_tax['tax_amount__sum']
            self.si_amount = items_total_amount
            self.tax_amount = items_total_tax_amount
            self.save()

    def __str__(self):
        return str(self.si_number)

class SaleInvoiceItem(models.Model):
    sale_invoice = models.ForeignKey(SaleInvoice, on_delete=models.CASCADE,verbose_name='Invoice Number')
    sale_order_item = models.ForeignKey(SaleOrderItem, on_delete=models.CASCADE,verbose_name='Item')
    bill_quantity = models.DecimalField(max_digits=14,decimal_places=2,default=0.00,verbose_name='Quantity')
    total_price = models.DecimalField(max_digits=14,decimal_places=2,default=0.00,verbose_name='Total Price')
    tax_rate = models.ForeignKey(Tax, on_delete=models.PROTECT)
    tax_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00,verbose_name='Tax Amount')
    total_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00,verbose_name='Total Amount')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.sale_order_item.item)
