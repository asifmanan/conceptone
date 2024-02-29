from django.shortcuts import render
from employeesApp.models import Employee
from django.urls import reverse, reverse_lazy
from employeesApp.forms import EmployeeForm, EmployeeSearchForm
from django.views.generic import CreateView, FormView
# Create your views here.
class CreateEmployee(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employeesapp/create_employee.html'
    def get_success_url(self):
        return reverse_lazy('employeesApp:ListEmployees')

class ListEmployees(FormView):
    form_class = EmployeeSearchForm
    template_name = 'employeesapp/list_employees.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['object_list'] = Employee.objects.all()
        return context
