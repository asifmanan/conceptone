from django import forms
from django.forms import (formset_factory, modelformset_factory)
from datetime import datetime
from crudbasic.models import (Projects,
                                TaxRate,
                                )
from crudbasic.basic_functions import get_col_heads

class TaxRateForm(forms.ModelForm):
    tax_value = forms.DecimalField(max_digits=5,decimal_places=2,initial=0.00,widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = TaxRate
        fields = '__all__'
        widgets = {
                'tax_name':forms.TextInput(attrs={'class':'form-control'}),
                'tax_code':forms.TextInput(attrs={'class':'form-control'}),
                'tax_jurisdiction':forms.Select(attrs={'class':'form-control'}),
                # 'tax_value':forms.NumberInput(attrs={'class':'form-control'}),
                }

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

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'
        widgets = {
                'project_customer':forms.Select(attrs={'class':'form-control'}),
                'project_code':forms.TextInput(attrs={'class':'form-control'}),
                'project_name':forms.TextInput(attrs={'class':'form-control'}),
                'project_city':forms.TextInput(attrs={'class':'form-control'}),
                'project_status':forms.Select(attrs={'class':'form-control'}),
        }


class BasicSearch(forms.Form):
    field_dct = {}
    search_by = forms.ChoiceField(choices=field_dct,widget=forms.Select(attrs={'class':'form-control form-control-sm'}))
    search_for = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))

    def __init__(self,*arg,**kwargs):
        caller = kwargs.pop('caller')
        super(BasicSearch, self).__init__(*arg,**kwargs)
        field_dct = get_col_heads(caller)
        self.fields['search_by'].choices = field_dct
