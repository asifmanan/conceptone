from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models import Sum, F
from crudbasic.models import Items, TaxRate, Projects
from suppliersApp.models import Supplier

class PurchaseOrder(models.Model):
    po_number = models.CharField(verbose_name='PO Number',max_length=48,blank=True)
    po_serial_number = models.IntegerField(blank=True,default=0)
    po_date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    project = models.ForeignKey(Projects, on_delete=models.PROTECT)
    po_amount = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    tax_rate = models.ForeignKey(TaxRate, on_delete=models.PROTECT)
    tax_amount = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    published = models.BooleanField(default=False)
    published_date = models.DateTimeField(blank=True, null=True)
    # po_payment_status
    read_status = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def publish(self):
        operation_success = False
        try:
            published_items = PurchaseOrder.objects.filter(published=True)
            if published_items.exists():
                purchase_order = published_items.order_by('po_serial_number').last()
                if purchase_order.read_status == 0:
                    purchase_order.read_status = F('read_status') + 1
                    purchase_order.save()
                    # purchase_order.refresh_from_db()
                    # print("Updated")
                    # print(purchase_order.read_status)
                    po_serial_number = purchase_order.po_serial_number
                    new_po_serial_number = po_serial_number + 1
                    self.po_serial_number = new_po_serial_number
                    self.publish_date = timezone.now()
                    self.published = True
                    self.save()
                    purchase_order.read_status = F('read_status') - 1
                    purchase_order.save()
                    operation_success = True
            else:
                if self.read_status == 0:
                    self.read_status = F('read_status') + 1
                    self.save()
                    self.po_serial_number = 1
                    self.publish_date = timezone.now()
                    self.published = True
                    self.read_status = 0
                    self.save()
                    operation_success=True
        except:
            print("Whoopss, The Program Enoutered an Error!")
            # Need to show error page to user and an option to retry
            # and go back to publish page.
        return operation_success

    def CalculatePoTotal(self):
        items = PurchaseOrderItem.objects.filter(purchase_order=self)
        if items.exists():
            items_sum = items.aggregate(Sum('total_price'))
            po_amount = items_sum['total_price__sum']
            tax_amount = po_amount*self.tax_rate.tax_value
            self.po_amount = po_amount
            self.tax_amount = tax_amount
            self.total_amount = po_amount + tax_amount
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
