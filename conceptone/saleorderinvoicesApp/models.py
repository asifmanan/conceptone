from django.db import models
from django.utils import timezone
from django.db.models import Sum
from saleordersApp.models import SaleOrder, SaleOrderItem
from baseApp.models import Company

# Create your models here.

class SaleOrderInvoice(models.Model):
    supplier = models.ForeignKey(Company, on_delete=models.PROTECT, blank=True)
    sale_order = models.ForeignKey(SaleOrder, on_delete=models.PROTECT)
    invoice_number = models.CharField(max_length=56, unique=True)
    invoice_date = models.DateField()
    amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    tax_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    total_amount = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def CalculateTotal(self):
        items = SaleOrderInvoiceItem.objects.filter(sale_order_invoice=self)
        if items.exists():
            items_sum = items.aggregate(Sum('amount'))
            invoice_items_sum = items_sum['amount__sum']
            items_tax = items.aggregate(Sum('tax_amount'))
            invoice_items_tax_sum = items_tax['tax_amount__sum']
            total_amount = invoice_items_sum+invoice_items_tax_sum
            self.amount = invoice_items_sum
            self.tax_amount = invoice_items_tax_sum
            self.total_amount = total_amount
            self.save()


    def __str__(self):
        return self.invoice_number

class PublishedSaleOrderInvoice(models.Model):
    invoice = models.OneToOneField(SaleOrderInvoice, on_delete=models.PROTECT, related_name='published_invoice')
    invoice_number = models.CharField(max_length=56, unique=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.invoice_number

    @classmethod
    def create(cls,unpublished_invoice):
        p_invoice = cls(invoice=unpublished_invoice)
        p_invoice.invoice_number=None
        p_invoice.save()
        p_invoice.invoice_number = p_invoice.PublishInvoice()
        p_invoice.save()
        if not p_invoice.invoice_number:
            del p_invoice
        return p_invoice

    def PublishInvoice(self,*args,**kwargs):
        if not self.invoice_number:
            invoice_year = self.invoice.invoice_date.strftime("%y")
            project_code = self.invoice.sale_order.buyer.customer_code
            invoice_uid = self.id + 10000
            invoice_number = str(invoice_year) + project_code + '-' + str(invoice_uid)
            # print(invoice_number)
            return invoice_number or None

class SaleOrderInvoiceItem(models.Model):
    sale_order_invoice = models.ForeignKey(SaleOrderInvoice, on_delete=models.CASCADE)
    item = models.ForeignKey(SaleOrderItem, on_delete=models.PROTECT)
    bill_quantity = models.DecimalField(max_digits=14,decimal_places=4)
    amount = models.DecimalField(max_digits=14,decimal_places=2)
    tax_amount = models.DecimalField(max_digits=14,decimal_places=2)
    total_amount = models.DecimalField(max_digits=14,decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def add_amount_to_saleorderinvoice(self):
        self.sale_order_invoice.amount += self.amount
        self.sale_order_invoice.tax_amount += self.tax_amount
        self.sale_order_invoice.total_amount += self.amount + self.tax_amount
        self.sale_order_invoice.save()

    def remove_amount_from_saleorderinvoice(self):
        self.sale_order_invoice.amount -= self.amount
        self.sale_order_invoice.tax_amount -= self.tax_amount
        self.sale_order_invoice.total_amount -= self.amount + self.tax_amount
        self.sale_order_invoice.save()
