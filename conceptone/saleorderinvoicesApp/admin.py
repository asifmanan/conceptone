from django.contrib import admin
from saleorderinvoicesApp.models import SaleOrderInvoice, PublishedSaleOrderInvoice
# Register your models here.
admin.site.register(SaleOrderInvoice)
admin.site.register(PublishedSaleOrderInvoice)
