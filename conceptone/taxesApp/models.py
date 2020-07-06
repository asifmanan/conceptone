from django.db import models
from baseApp.models import Province

# Create your models here.
class TaxAuthority(models.Model):
    authority_code = models.CharField(max_length=16)
    authority_display_name = models.CharField(max_length=16)
    authority_name = models.CharField(max_length=256)
    authority_jurisdiction = models.ForeignKey(Province,on_delete=models.PROTECT)
    authority_address = models.CharField(max_length=512)
    authority_phone = models.CharField(max_length=128)
    authority_email = models.CharField(max_length=128)

    def __str__(self):
        return self.authority_name

class Tax(models.Model):
    tax_code = models.CharField(max_length=16)
    tax_display_name = models.CharField(max_length=16)
    tax_description = models.CharField(max_length=512)
    tax_value = models.DecimalField(max_digits=5,decimal_places=2)
    tax_authority = models.ForeignKey(TaxAuthority,on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tax_code
