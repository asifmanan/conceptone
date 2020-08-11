from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.forms import modelformset_factory
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
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
                                        invoice_item_formset,
                                        SaleOrderInvoiceItemForm,
                                        )

class NewSaleOrderInvoice(TemplateView):
    template_name = 'saleorderinvoicesapp/create_saleorderinvoice.html'
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        form = SaleOrderInvoiceForm()
        form.fields.pop('invoice_number')
        form.fields.pop('invoice_date')
        context['form'] = form
        return context

# AJAX CALL
def SelectSupplier(request):
    if request.POST.get('company') == "":
        data = 0
        form = SaleOrderInvoiceForm()
        form.fields.pop('invoice_number')
        form.fields.pop('invoice_date')
        return render(request,'saleorderinvoicesapp/_form_saleorderinvoice1.html',{'form':form})

    company_id = request.POST.get('company')
    request.session['so_invoice_company'] = company_id
    sale_order_list = SaleOrder.objects.filter(supplier__id=company_id)
    form = SaleOrderInvoiceForm()
    form.fields['sale_order'].queryset = sale_order_list
    form.fields['supplier'].initial = company_id
    form.fields['supplier'].disabled = True
    form.fields['sale_order'].widget.attrs.pop('disabled')
    # form.fields['invoice_number'].widget.attrs.pop('disabled')
    # form.fields['invoice_date'].widget.attrs.pop('disabled')
    form.fields.pop('invoice_number')
    form.fields.pop('invoice_date')
    return render(request,'saleorderinvoicesapp/_form_saleorderinvoice1.html',{'form':form})

# AJAX CALL
def SelectSaleOrder(request):
    if request.POST.get('sale_order') == "":
        data = 0
        form = SaleOrderInvoiceForm()
        return render(request,'saleorderinvoicesapp/_form_saleorderinvoice1.html',{'form',form})
    if 'so_invoice_company' in request.session:
        initial_selected_company = request.session['so_invoice_company']
        sale_order_id = request.POST.get('sale_order')
        sale_order_item_list = SaleOrderItem.objects.filter(sale_order__id=sale_order_id)
        if sale_order_item_list.exists():
            company_id = str(sale_order_item_list.first().sale_order.supplier.id)
            if initial_selected_company==company_id:
                request.session["so_invoice_saleorder"] = sale_order_id
        else:
            print("Error SaleOrder Company does not match")
        form = SaleOrderInvoiceForm()
        form.fields['sale_order'].initial = sale_order_id
        form.fields['supplier'].initial = company_id
        form.fields['sale_order'].disabled = True
        form.fields['supplier'].disabled = True
        form.fields.pop('invoice_number')
        form.fields.pop('invoice_date')
        sale_order_id = request.POST.get('sale_order')
        object_list = sale_order_item_list
        return render(request,'saleorderinvoicesapp/_form_saleorderinvoice1.html',{'form':form,'object_list':object_list})
    else:
        form = SaleOrderInvoiceForm()
        return render(request,'saleorderinvoicesapp/_form_saleorderinvoice1.html',{'form':form})

def SelectSaleOrderItem(request):
    selected_item_list = request.POST.getlist('sale_order_item[]')
    if selected_item_list:
        print(selected_item_list)
        request.session["so_invoice_selected_item"] = selected_item_list
        print(request.session["so_invoice_selected_item"])
        url = reverse('saleorderinvoicesApp:CreateSaleOrderInvoiceItem')
        data={
            'url':url,
            'status':'OK',
        }
        print("url: ",url)
    elif not selected_item_list:
        data={
            'status':'FAIL',
        }
        print("List is empty")
    return JsonResponse(data)

class CreateSaleOrderInvoiceItem(FormView):
    model = SaleOrderInvoiceItem
    form_class = invoice_item_formset
    template_name = 'saleorderinvoicesapp/createsaleorderinvoiceitem.html'
    def get(self,request,*args,**kwargs):
        if 'so_invoice_selected_item' not in self.request.session:
            return redirect('saleorderinvoicesApp:NewSaleOrderInvoice')
        return super().get(request,*args,**kwargs)

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        id_selected_item = self.request.session.pop('so_invoice_selected_item')
        line_item = SaleOrderItem.objects.filter(id__in=id_selected_item)
        sale_order = line_item.first().sale_order
        no_of_items = len(id_selected_item)
        formdata={
            'form-TOTAL_FORMS': no_of_items,
            'form-INITIAL_FORMS': '0',
            'form-MAX_NUM_FORMS': '',
        }
        item_formset = invoice_item_formset(formdata)
        form_list = []
        for form in item_formset:
            element = {
                'bill_quantity':form['bill_quantity'],
            }
            form_list.append(element)
        i=0
        for item in line_item:
            item.form=form_list[i]
            i=i+1

        context['line_item'] = line_item
        context['sale_order'] = sale_order
        context['buyer'] = sale_order.buyer
        context['project'] = sale_order.project

        return context

class ListSaleOrderInvioce(FormView):
    form_class = SaleOrderInvoiceSearchForm
    template_name = 'saleorderinvoicesApp/list_saleorderinvoice.html'
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['object_list'] = SaleOrderInvoice.objects.all().order_by('invoice_date')
        return context
