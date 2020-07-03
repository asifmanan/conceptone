from django.contrib import admin
from crudbasic.models import Projects, TaxRate
from customersApp.models import Customer
from suppliersApp.models import Supplier
from itemsApp.models import Item
# Register your models here.
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Projects)
admin.site.register(Item)
admin.site.register(TaxRate)
