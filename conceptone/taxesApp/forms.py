from django import forms
from taxesApp.models import Tax, TaxAuthority

class TaxForm(forms.ModelForm):
    class Meta:
        model = Tax
        fields = ('tax_code',
                    'tax_description',
                    'tax_value',
                    'tax_authority',
        )
        widgets={
            'tax_code':forms.TextInput(attrs={'class':'form-control'}),
            'tax_authority':forms.Select(attrs={'class':'form-control'}),
            'tax_description':forms.TextInput(attrs={'class':'form-control'}),
            'tax_value':forms.TextInput(attrs={'class':'form-control'}),
        }

class TaxAuthorityForm(forms.ModelForm):
    class Meta:
        model = TaxAuthority
        fields = ('authority_code',
                    'authority_name',
                    'authority_jurisdiction',
                    'authority_address',
                    'authority_phone',
                    'authority_email',
        )
        widgets={
            'authority_code':forms.TextInput(attrs={'class':'form-control'}),
            'authority_jurisdiction':forms.Select(attrs={'class':'form-control'}),
            'authority_name':forms.TextInput(attrs={'class':'form-control'}),
            'authority_address':forms.TextInput(attrs={'class':'form-control'}),
            'authority_phone':forms.TextInput(attrs={'class':'form-control'}),
            'authority_email':forms.TextInput(attrs={'class':'form-control'}),
        }
