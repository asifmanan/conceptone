from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models import Sum

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=16)
    po_date = models.DateField()
    po_supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    po_amount = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    po_tax = models.ForeignKey(TaxRate, on_delete=models.PROTECT)
    po_tax_amount = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    po_draft = models.BooleanField(default=True)
    po_publish = models.BooleanField(default=False)
    po_publish_date = models.DateTimeField(blank=True, null=True)
    # po_payment_status
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def publish(self):
        self.po_publish_date = timezone.now()
        self.po_publish = True
        self.save()

    def CalculatePoTotal(self):
        items = OrderItem.objects.filter(po_number=self)
        if items.exists():
            items_sum = items.aggregate(Sum('total_price'))
            # print(items_sum['total_price__sum'])
            items_total_amount = items_sum['total_price__sum']
            self.po_amount = items_total_amount
            print(self.po_tax.tax_value)
            self.po_tax_amount = items_total_amount*self.po_tax.tax_value
            self.save()

    def __str__(self):
        return self.po_number

class OrderItem(models.Model):
    po_line_number = models.IntegerField(verbose_name='Line')
    order_item = models.ForeignKey(Items, on_delete=models.PROTECT,verbose_name='Item')
    po_number = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    order_quantity = models.DecimalField(max_digits=14, decimal_places=2,verbose_name='Quantity')
    purchase_price = models.DecimalField(max_digits=14, decimal_places=2,verbose_name='Purchase Price')
    total_price = models.DecimalField(max_digits=14, decimal_places=2)
    variation_number = models.IntegerField(default=0)
    variation_quantity = models.DecimalField(max_digits=14, decimal_places=2,default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.po_line_number)
