from django.contrib import admin
from crudbasic.models import Customers, Suppliers, Projects, Items
# Register your models here.
admin.site.register(Customers)
admin.site.register(Suppliers)
admin.site.register(Projects)
admin.site.register(Items)
