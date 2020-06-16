from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models import Sum
from crudbasic.models import Customers, Items, TaxRate, Projects, Suppliers

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=16)
    po_date = models.DateField()
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.PROTECT)
    po_amount = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    tax_rate = models.ForeignKey(TaxRate, on_delete=models.PROTECT)
    tax_amount = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    published = models.BooleanField(default=False)
    published_date = models.DateTimeField(blank=True, null=True)
    # po_payment_status
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.published = True
        self.save()

    def CalculatePoTotal(self):
        items = PurchaseOrderItem.objects.filter(purchase_order=self)
        if items.exists():
            items_sum = items.aggregate(Sum('total_price'))
            po_amount = items_sum['total_price__sum']
            tax_amount = po_amount*self.tax_rate.tax_value
            self.po_amount = po_amount
            self.tax_amount = tax_amount
            self.total_amount = po_amount + tax_amount
            # print(self.po_tax.tax_value)
            self.save()

    def __str__(self):
        return self.po_number

class PurchaseOrderItem(models.Model):
    po_line_number = models.IntegerField(verbose_name='Line')
    item = models.ForeignKey(Items, on_delete=models.PROTECT,verbose_name='Item')
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    order_quantity = models.DecimalField(max_digits=14, decimal_places=2,verbose_name='Quantity')
    purchase_price = models.DecimalField(max_digits=14, decimal_places=2,verbose_name='Purchase Price')
    total_price = models.DecimalField(max_digits=14, decimal_places=2)
    variation_number = models.IntegerField(default=0)
    variation_quantity = models.DecimalField(max_digits=14, decimal_places=2,default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.po_line_number)
