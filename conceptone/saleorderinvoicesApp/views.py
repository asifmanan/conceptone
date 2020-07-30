from django.shortcuts import render, get_object_or_404, render_to_response
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django import forms
from django.views.generic import (
                                CreateView,
                                DeleteView,
                                FormView,
                                TemplateView,
                                UpdateView,
                                View,
                                )
from saleordersApp.models import (
                                SaleOrder,
                                SaleOrderItem,
                                )
from saleorderinvoicesApp.models import (
                                        SaleOrderInvoice,
                                        SaleOrderInvoiceItem,
                                        )
from saleorderinvoicesApp.forms import (
                                        SaleOrderInvoiceForm,
                                        SaleOrderInvoiceSearchForm,
                                        SupplierSelectForm,
                                        )
# Create view for SaleOrderInvoice.
class CreateSaleOrderInvoice(CreateView):
    model = SaleOrderInvoice
    form_class = SaleOrderInvoiceForm
    template_name = 'saleorderinvoicesapp/create_saleorderinvoice.html'

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():
            sale_order_invoice = form.save(commit=False)
            sale_order_invoice.supplier = sale_order_invoice.sale_order.supplier
            sale_order_invoice.save()
            return HttpResponseRedirect(reverse_lazy('baseApp:index'))
        return render(request, self.template_name,{'form':form})

# AJAX CALL
def SelectSupplier(request):
    if request.POST.get('company') == "":
        data = 0
        form = SaleOrderInvoiceForm()
        return render(request,'saleorderinvoicesapp/_form_saleorderinvoice1.html',{'form':form})
    if 'company' in request.POST:
        print("yayyyy")

    company_id = request.POST.get('company')
    sale_order_list = SaleOrder.objects.filter(supplier__id=company_id)
    form = SaleOrderInvoiceForm()
    form.fields['sale_order'].queryset = sale_order_list
    form.fields['supplier'].initial = company_id
    form.fields['supplier'].disabled = True
    form.fields['sale_order'].widget.attrs.pop('disabled')
    form.fields['invoice_number'].widget.attrs.pop('disabled')
    form.fields['invoice_date'].widget.attrs.pop('disabled')
    # print(request.method)
    return render(request,'saleorderinvoicesapp/_form_saleorderinvoice1.html',{'form':form})

def SelectSaleOrder(request):
    if request.POST.get('sale_order') == "":
        data = 0
        form = SaleOrderInvoiceForm()
        return render(request,'saleorderinvoicesapp/_form_saleorderinvoice1.html',{'form',form})
    sale_order_id = request.POST.get('sale_order')
    sale_order_item_list = SaleOrderItem.objects.filter(sale_order__id=sale_order_id)
    if sale_order_item_list.exists():
        company_id = sale_order_item_list.first().sale_order.supplier.id
    form = SaleOrderInvoiceForm()
    form.fields['sale_order'].initial = sale_order_id
    form.fields['supplier'].initial = company_id
    form.fields['sale_order'].disabled = True
    form.fields['supplier'].disabled = True
    sale_order_id = request.POST.get('sale_order')

    if sale_order_item_list.exists():
        company_id = sale_order_item_list.first().sale_order.supplier.id
        print(company_id)
    return render(request,'saleorderinvoicesapp/_form_saleorderinvoice1.html',{'form':form})

class ListSaleOrderInvioce(FormView):
    form_class = SaleOrderInvoiceSearchForm
    template_name = 'saleorderinvoicesApp/list_saleorderinvoice.html'
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['object_list'] = SaleOrderInvoice.objects.all().order_by('invoice_date')
        return context
