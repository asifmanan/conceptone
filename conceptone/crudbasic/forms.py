from django import forms
from crudbasic.models import Customers, Projects, Items

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

class CustomerSearch(forms.Form):
    search_by = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}))
    search_for = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'
        widgets = {
                'customer':forms.Select(attrs={'class':'form-control'}),
                'project_id':forms.TextInput(attrs={'class':'form-control'}),
                'project_name':forms.TextInput(attrs={'class':'form-control'}),
                'project_city':forms.TextInput(attrs={'class':'form-control'}),
                'project_worth':forms.TextInput(attrs={'class':'form-control'}),

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
