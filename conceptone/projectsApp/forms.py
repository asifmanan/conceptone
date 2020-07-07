from django import forms
from projectsApp.models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
                    'company',
                    'project_code',
                    'project_name',
                    'customer',
                    'project_status',
                    'contract_number',
                    'contract_signing_date',
                    'award_date',
                    'delivery_date',
                    )
        widgets = {
                'company':forms.Select(attrs={'class':'form-control'}),
                'project_code':forms.TextInput(attrs={'class':'form-control'}),
                'project_name':forms.TextInput(attrs={'class':'form-control'}),
                'customer':forms.Select(attrs={'class':'form-control'}),
                'project_status':forms.Select(attrs={'class':'form-control'}),
                'contract_number':forms.TextInput(attrs={'class':'form-control'}),
                'contract_signing_date':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
                'award_date':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
                'delivery_date':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }

class ProjectSearchForm(forms.Form):
    company = forms.CharField(label='Company', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control search_field'}))
    project_code = forms.CharField(label='Project Code', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control search_field'}))
    project_name = forms.CharField(label='Project Name', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control search_field'}))
    customer = forms.CharField(label='Customer', max_length=60, required=False, widget=forms.TextInput(attrs={'class':'form-control search_field'}))
