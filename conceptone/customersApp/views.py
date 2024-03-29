from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from customersApp.models import Customer
from customersApp.forms import CustomerForm, CustomerSearchForm
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, FormView
# Create your views here.
class CreateCustomer(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customersapp/create_customer.html'
    def get_success_url(self):
        return reverse_lazy('customersApp:ListCustomers')

class ListCustomers(FormView):
    form_class = CustomerSearchForm
    template_name = 'customersapp/list_customers.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['object_list'] = Customer.objects.all()
        return context

# class UpdateCustomerView(UpdateView):
#     model = Customer
#     form_class = CustomerForm
#     template_name = 'customersapp/create_customer.html'
#
#     def get_success_url(self):
#         return reverse('customersApp:ListCustomers')

def CustomerQuery(request):
    data = request.GET
    query_result = Customer.objects.all()
    if data['customer_name'] != '':
        query_result = query_result.filter(customer_name__icontains=data['customer_name'])
    if data['customer_ntn_number'] != '':
        query_result = query_result.filter(customer_ntn_number__icontains=data['customer_ntn_number'])
    if data['customer_phone'] != '':
        # print(data['po_date'])
        query_result = query_result.filter(customer_phone__icontains=data['customer_phone'])
    if data['customer_code'] != '':
        query_result = query_result.filter(customer_code__icontains=data['customer_code'])
    new_html_table = render_to_string('customersApp/tables/list_customerstable.html',{'object_list':query_result})
    return HttpResponse(new_html_table)
