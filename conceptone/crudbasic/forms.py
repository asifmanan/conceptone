from django import forms
from django.forms import (formset_factory, modelformset_factory)
from datetime import datetime
from crudbasic.models import (Projects,
                                )


# if using formset then unindent the following
# OrderItem_Formset = modelformset_factory(
#     OrderItem,
#     fields=('po_line_number','order_item','order_quantity','purchase_price','total_price' ),
#     extra=1,
#     widgets={
#             'po_line_number':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
#             'order_item':forms.Select(attrs={'class':'form-control form-control-sm', 'type':'date'}),
#             'order_quantity':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
#             'purchase_price':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
#             'total_price':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
#             }
#        )
