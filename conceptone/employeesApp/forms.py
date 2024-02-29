from django import forms
from employeesApp.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = (
                    'first_name','last_name','gender','dob',
                    'cnic_number','employee_id',
                    'address','city','phone_1','phone_2',
                    'email_1','email_2',
                    'company','department','designation','joining_date',
                    )
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'dob':forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'cnic_number':forms.TextInput(attrs={'class':'form-control'}),
            'employee_id':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.Select(attrs={'class':'form-control'}),
            'phone_1':forms.TextInput(attrs={'class':'form-control'}),
            'phone_2':forms.TextInput(attrs={'class':'form-control'}),
            'email_1':forms.TextInput(attrs={'class':'form-control'}),
            'email_2':forms.TextInput(attrs={'class':'form-control'}),
            'company':forms.Select(attrs={'class':'form-control'}),
            'department':forms.Select(attrs={'class':'form-control'}),
            'designation':forms.TextInput(attrs={'class':'form-control'}),
            'joining_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
        }

class EmployeeSearchForm(forms.Form):
    employee_name = forms.CharField(label='Employee name', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control search_field'}))
    employee_id = forms.CharField(label='Employee Id', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control search_field'}))
    department = forms.CharField(label='Department', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control search_field'}))
    phone = forms.CharField(label='Phone number', max_length=60, required=False, widget=forms.TextInput(attrs={'class':'form-control search_field'}))
