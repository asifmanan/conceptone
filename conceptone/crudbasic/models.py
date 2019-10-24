from django.db import models
from django.urls import reverse

# Create your models here.
class Customers(models.Model):
    customer_code = models.CharField(max_length=16, unique=True)
    customer_name = models.CharField(max_length=128, unique=True)
    customer_address = models.CharField(max_length=264)
    customer_city = models.CharField(max_length=128)
    customer_phone = models.CharField(max_length=128, blank=True)
    customer_fax = models.CharField(max_length=128, blank=True)
    customer_email = models.EmailField(max_length=192, blank=True)
    customer_ntn_number = models.CharField(max_length=128, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_name

    def this_class_name(self):
        return 'Customer'

    # def get_absolute_url(self):
    #     if 'save' in request.POST:
    #         print('Save was Clicked')
    #     return reverse('crudbasic:customers')

class Suppliers(models.Model):
    supplier_code = models.CharField(max_length=16, unique=True)
    supplier_name = models.CharField(max_length=128, unique=True)
    supplier_address = models.CharField(max_length=264)
    supplier_city = models.CharField(max_length=128)
    supplier_phone = models.CharField(max_length=128, blank=True)
    supplier_fax = models.CharField(max_length=128, blank=True)
    supplier_email = models.EmailField(max_length=192, blank=True)
    supplier_ntn_number = models.CharField(max_length=128, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def this_class_name(self):
        return 'Supplier'

    def __str__(self):
        return self.supplier_name

class Projects(models.Model):
    status_flags = [
        ('Prospective','Prospective'),
        ('Completed','Completed'),
        ('On-Going','On-Going'),
    ]
    project_code = models.CharField(max_length=16, unique=True)
    project_name = models.CharField(max_length=128, unique=True)
    project_customer = models.ForeignKey(Customers, on_delete=models.PROTECT)
    project_city = models.CharField(max_length=128)
    project_status = models.CharField(max_length=16,choices=status_flags)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name

    def this_class_name(self):
        return 'Project'

class Items(models.Model):
    item_type_choices = [
        ('Goods', 'Goods'),
        ('Services', 'Services'),
    ]
    item_code = models.CharField(max_length=16, unique=True)
    item_description = models.CharField(max_length=192)
    item_uom = models.CharField(max_length=16)
    item_type = models.CharField(max_length=8, choices=item_type_choices)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_description

    def this_class_name(self):
        return 'Item'

class TaxRate(models.Model):
    tax_code = models.CharField(max_length=16)
    tax_name = models.CharField(max_length=64)
    tax_value = models.DecimalField(max_digits=5, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tax_name

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=16)
    po_date = models.DateField()
    po_supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    po_amount = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    po_tax = models.ForeignKey(TaxRate, on_delete=models.PROTECT)
    po_draft = models.BooleanField(default=True)
    # po_payment_status
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    po_line_number = models.CharField(max_length=16)
    order_item = models.ForeignKey(Items, on_delete=models.PROTECT)
    po_number = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    order_quantity = models.DecimalField(max_digits=14, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=14, decimal_places=2)
    total_price = models.DecimalField(max_digits=14, decimal_places=2)
    variation_number = models.IntegerField(default=0)
    variation_quantity = models.DecimalField(max_digits=14, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.po_line_number

# class AccountsTable(models.Model):
