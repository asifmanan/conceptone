from django.db import models
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    item_type_choices = [
        ('GD', 'Goods'),
        ('SE', 'Services'),
    ]
    item_sub_type_choices = [
        ('TS', 'Trade stock'),
        ('CS', 'Consumable Stock'),
        ('FA', 'Fixed Asset'),
    ]

    item_code = models.CharField(max_length=16, unique=True)
    item_description = models.CharField(max_length=192)
    item_uom = models.CharField(max_length=16)
    item_price = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    item_type = models.CharField(max_length=8, choices=item_type_choices)
    item_sub_type = models.CharField(max_length=2, choices=item_sub_type_choices,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_description

    def this_class_name(self):
        return 'Item'
