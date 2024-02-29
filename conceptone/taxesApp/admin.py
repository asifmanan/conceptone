from django.contrib import admin
from taxesApp.models import Tax,TaxAuthority

# Register your models here.
admin.site.register(Tax)
admin.site.register(TaxAuthority)
