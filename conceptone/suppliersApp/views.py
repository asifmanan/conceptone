from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from suppliersApp.models import Supplier
from suppliersApp.forms import SupplierForm, SupplierSearchForm
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView,
                                    FormView,
                                    UpdateView)
# Create your views here.
class CreateSupplier(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'suppliersapp/create_supplier.html'
    def get_success_url(self):
        return reverse_lazy('suppliersApp:ListSuppliers')

class ListSuppliers(FormView):
    form_class = SupplierSearchForm
    template_name = 'suppliersapp/list_suppliers.html'
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['object_list'] = Supplier.objects.all()
        return context

# class DeleteSupplierView(DeleteView):
#     model = Suppliers
#     success_url = reverse_lazy('crudbasic:suppliers')
#     template_name = 'crudbasic/dialog/objdelconf.html'

# class UpdateSupplierView(UpdateView):
#     model = Suppliers
#     form_class = SupplierForm
#     template_name = 'suppliersapp/create_supplier.html'
#
#     def get_success_url(self):
#         return reverse('crudbasic:suppliers')

def SupplierQuery(request):
    data = request.GET
    query_result = Supplier.objects.all()
    if data['supplier_name'] != '':
        query_result = query_result.filter(supplier_name__icontains=data['supplier_name'])
    if data['supplier_ntn_number'] != '':
        query_result = query_result.filter(supplier_ntn_number__icontains=data['supplier_ntn_number'])
    if data['supplier_phone'] != '':
        query_result = query_result.filter(supplier_phone__range=data['supplier_phone'])
    if data['supplier_code'] != '':
        query_result = query_result.filter(supplier_code__icontains=data['supplier_code'])
    new_html_table = render_to_string('suppliersApp/tables/list_supplierstable.html',{'object_list':query_result})
    return HttpResponse(new_html_table)
