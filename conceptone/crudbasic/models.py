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

    def __str__(self):
        return self.customer_name

class Projects(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    project_id = models.CharField(max_length=16, unique=True)
    project_name = models.CharField(max_length=128, unique=True)
    project_city = models.CharField(max_length=128)
    project_worth = models.DecimalField(max_digits=10, decimal_places=2,default=0.00, blank=True)

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

    def __str__(self):
        return self.item_description