from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.db.models import Sum
from customersApp.models import Customer
from projectsApp.models import Project
from baseApp.models import Company
from itemsApp.models import Item
from taxesApp.models import Tax
# Create your models here.
class SaleOrder(models.Model):
    supplier = models.ForeignKey(Company, on_delete=models.PROTECT)
    so_number = models.CharField(max_length=56)
    so_date = models.DateField()
    buyer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    buyer_po_number = models.CharField(max_length=56)
    buyer_po_date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=14, decimal_places=2,default=0.00)
    tax_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    total_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    def CalculateSaleOrderTotal(self):
        items = SaleOrderItem.objects.filter(sale_order=self)
        if items.exists():
            items_sum = items.aggregate(Sum('amount'))
            saleorder_items_sum = items_sum['amount__sum']
            items_tax = items.aggregate(Sum('tax_amount'))
            saleorder_items_tax_sum = items_tax['tax_amount__sum']
            total_amount = saleorder_items_sum+saleorder_items_tax_sum
            self.amount = saleorder_items_sum
            self.tax_amount = saleorder_items_tax_sum
            self.total_amount = total_amount
            self.save()

    def __str__(self):
        return self.so_number

class SaleOrderItem(models.Model):
    line_number = models.IntegerField()
    sale_order = models.ForeignKey(SaleOrder, on_delete=models.PROTECT)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    tax = models.ForeignKey(Tax, on_delete=models.PROTECT)
    order_quantity = models.DecimalField(max_digits=14,decimal_places=2)
    sale_price = models.DecimalField(max_digits=14,decimal_places=2)
    amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    tax_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    total_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def add_amount_to_saleorder(self):
        self.sale_order.amount += self.amount
        self.sale_order.tax_amount += self.tax_amount
        self.sale_order.total_amount += self.amount+self.tax_amount
        self.sale_order.save()

    def remove_amount_from_saleorder(self):
        self.sale_order.amount -= self.amount
        self.sale_order.tax_amount -= self.tax_amount
        self.sale_order.total_amount -= self.amount+self.tax_amount
        self.sale_order.save()


    def __str__(self):
        return str(self.line_number)+self.item.item_code
