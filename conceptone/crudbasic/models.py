from django.db import models

# Create your models here.
class Customers(models.Model):
    customer_id = models.CharField(max_length=16, unique=True)
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

class Suppliers(models.Model):
    supplier_id = models.CharField(max_length=16, unique=True)
    supplier_name = models.CharField(max_length=128, unique=True)
    supplier_address = models.CharField(max_length=264)
    supplier_city = models.CharField(max_length=128)
    supplier_phone = models.CharField(max_length=128, blank=True)
    supplier_fax = models.CharField(max_length=128, blank=True)
    supplier_email = models.EmailField(max_length=192, blank=True)
    supplier_ntn_number = models.CharField(max_length=128, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # def get_col_heads(self):
    #     all_fields = self._meta.fields
    #     field_list = []
    #     for fields in all_fields:
    #         column_head = (str(fields)).split(".")
    #         print(column_head[-1])
    #         # field_list.append(column_head[-1])
    #     return field_list

    def __str__(self):
        return self.partner_name

class Projects(models.Model):
    status_flags = [
        ('Prospective','Prospective'),
        ('Completed','Completed'),
        ('On-Going','On-Going'),
    ]
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    project_id = models.CharField(max_length=16, unique=True)
    project_name = models.CharField(max_length=128, unique=True)
    project_city = models.CharField(max_length=128)
    project_status = models.CharField(max_length=16,choices=status_flags)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name

class Items(models.Model):
    item_type_choices = [
        ('Goods', 'Goods'),
        ('Services', 'Services'),
    ]
    item_line = models.CharField(max_length=16, unique=True)
    item_description = models.CharField(max_length=192)
    item_uom = models.CharField(max_length=16)
    item_type = models.CharField(max_length=8, choices=item_type_choices)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_description
