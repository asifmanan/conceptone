from django.contrib import admin
from crudbasic.models import Projects, Items, TaxRate
from customersApp.models import Customer
from suppliersApp.models import Supplier
# Register your models here.
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Projects)
admin.site.register(Items)
admin.site.register(TaxRate)
