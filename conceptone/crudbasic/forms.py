from django import forms
from crudbasic.models import Customers, Suppliers, Projects, Items
from crudbasic.basic_functions import get_col_heads

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'
        widgets = {
                'customer_id':forms.TextInput(attrs={'class':'form-control'}),
                'customer_name':forms.TextInput(attrs={'class':'form-control'}),
                'customer_address':forms.TextInput(attrs={'class':'form-control'}),
                'customer_city':forms.TextInput(attrs={'class':'form-control'}),
                'customer_phone':forms.TextInput(attrs={'class':'form-control'}),
                'customer_fax':forms.TextInput(attrs={'class':'form-control'}),
                'customer_email':forms.TextInput(attrs={'class':'form-control'}),
                'customer_ntn_number':forms.TextInput(attrs={'class':'form-control'}),
        }

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Suppliers
        fields = '__all__'
        widgets = {
                'supplier_id':forms.TextInput(attrs={'class':'form-control'}),
                'supplier_name':forms.TextInput(attrs={'class':'form-control'}),
                'supplier_address':forms.TextInput(attrs={'class':'form-control'}),
                'supplier_city':forms.TextInput(attrs={'class':'form-control'}),
                'supplier_phone':forms.TextInput(attrs={'class':'form-control'}),
                'supplier_fax':forms.TextInput(attrs={'class':'form-control'}),
                'supplier_email':forms.TextInput(attrs={'class':'form-control'}),
                'supplier_ntn_number':forms.TextInput(attrs={'class':'form-control'}),
        }

class BasicSearch(forms.Form):
    field_dct = {}
    search_by = forms.ChoiceField(choices=field_dct,widget=forms.Select(attrs={'class':'form-control'}))
    search_for = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    def __init__(self,arg):
        caller = arg
        if caller == 'customer':
            print("It Works!")
        cu = Customers()
        field_dct = get_col_heads(cu)
        self.fields['search_by'] = forms.ChoiceField(choices=field_dct,widget=forms.Select(attrs={'class':'form-control'}))

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'
        widgets = {
                'customer':forms.Select(attrs={'class':'form-control'}),
                'project_id':forms.TextInput(attrs={'class':'form-control'}),
                'project_name':forms.TextInput(attrs={'class':'form-control'}),
                'project_city':forms.TextInput(attrs={'class':'form-control'}),
                'project_status':forms.Select(attrs={'class':'form-control'}),

        }
class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = '__all__'
        widgets = {
                'item_line':forms.TextInput(attrs={'class':'form-control'}),
                'item_description':forms.TextInput(attrs={'class':'form-control'}),
                'item_uom':forms.TextInput(attrs={'class':'form-control'}),
                'item_type':forms.Select(attrs={'class':'form-control'}),
        }
