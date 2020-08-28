from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.forms import modelformset_factory
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import (
                                CreateView,
                                DetailView,
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
                                        SaleOrderInvoiceItemForm,
                                        SaleOrderInvoiceItemFormset,
                                        CreateSaleOrderInvoiceForm,
                                        )

class NewSaleOrderInvoice(TemplateView):
    template_name = 'saleorderinvoicesapp/newsaleorderinvoice.html'
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        form = SaleOrderInvoiceForm()
        form.fields.pop('invoice_number')
        form.fields.pop('invoice_date')
        context['form'] = form
        return context

class CreateSaleOrderInvoiceItem(FormView):
    model = SaleOrderInvoiceItem
    form_class = SaleOrderInvoiceItemForm
    template_name = 'saleorderinvoicesapp/createsaleorderinvoiceitem.html'
    def get(self,request,*args,**kwargs):
        if 'so_invoice_selected_item' and 'so_invoice_saleorder' and 'so_invoice_company' not in self.request.session:
            return redirect('saleorderinvoicesApp:NewSaleOrderInvoice')
        return super().get(request,*args,**kwargs)

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        line_item,sale_order = self.acquire_saleorder_data(*args,**kwargs)
        no_of_items = len(line_item)

        formdata={
            'form-TOTAL_FORMS': no_of_items,
            'form-INITIAL_FORMS': '0',
            'form-MAX_NUM_FORMS': '',
        }
        item_formset = SaleOrderInvoiceItemFormset(formdata)
        data = {
                'line_item':line_item,
                'item_formset':item_formset,
                }
        line_item = self.encapsulate_formset(**data)


        invoice_form = CreateSaleOrderInvoiceForm()
        context['invoice_form'] = invoice_form
        context['formset'] = item_formset
        context['line_item'] = line_item
        context['sale_order'] = sale_order
        context['buyer'] = sale_order.buyer
        context['project'] = sale_order.project

        return context

    def encapsulate_formset(self,**kwargs):
        form_list = []
        for form in kwargs['item_formset']:
            element = {
                'bill_quantity':form['bill_quantity'],
                'id_form' : form['id'],
            }
            form_list.append(element)
        i=0
        for item in kwargs['line_item']:
            item.form=form_list[i]
            i=i+1
        return kwargs['line_item']


    def acquire_saleorder_data(self,*args,**kwargs):
        id_selected_item = self.request.session['so_invoice_selected_item']
        line_item = SaleOrderItem.objects.filter(id__in=id_selected_item)
        sale_order = line_item.first().sale_order
        return (line_item,sale_order)

    def post(self,request,*args,**kwargs):
        invoice_form = CreateSaleOrderInvoiceForm(self.request.POST)
        item_formset = SaleOrderInvoiceItemFormset(self.request.POST)

        if item_formset.is_valid():
            invalid_flag = False
            item_formset_data = item_formset.cleaned_data
            line_item,sale_order = self.acquire_saleorder_data(**kwargs)
            for item_form_qty, so_item_qty in zip(item_formset_data,line_item):
                if item_form_qty['bill_quantity'] <= so_item_qty.order_quantity:
                    pass
                elif item_form_qty['bill_quantity'] > so_item_qty.order_quantity:
                    invalid_flag = True
                    messages.warning(self.request,"One of more BILL QUANTITY is greater than ORDER QUANTITY.")
        elif not item_formset.is_valid():
            messages.warning(self.request,"One of more values in BILL QUANTITIES are invalid.")
            invalid_flag = True

        if not invoice_form.is_valid():
            invalid_flag = True

        if invalid_flag:
            return self.form_invalid(invoice_form,item_formset)
        else:
            return self.form_valid(invoice_form,item_formset)

    def form_invalid(self,invoice_form,item_formset,**kwargs):
        context = self.get_context_data(**kwargs)
        line_item = context['line_item']
        data = {
                'line_item':line_item,
                'item_formset':item_formset,
                }
        line_item = self.encapsulate_formset(**data)
        context['invoice_form'] = invoice_form
        context['line_item'] = line_item
        return self.render_to_response(context)

    def form_valid(self,invoice_form,item_formset,*arg,**kwargs):
        line_item, sale_order = self.acquire_saleorder_data(**kwargs)
        invoice_form_data = invoice_form.cleaned_data
        invoice_number = invoice_form_data['invoice_number']
        invoice_date = invoice_form_data['invoice_date']
        # creating invoice
        invoice = SaleOrderInvoice()
        invoice.invoice_number = invoice_number
        invoice.invoice_date = invoice_date
        invoice.sale_order = sale_order
        invoice.buyer = sale_order.buyer
        invoice.supplier = sale_order.supplier
        invoice.save()
        # try:
        # for item in line_item:
        #     print(item.sale_price)
        #Creating Invoice Line Items
        for form, item in zip(item_formset,line_item):
            invoice_line_item = form.save(commit=False)
            invoice_line_item.sale_order_invoice = invoice
            invoice_line_item.item = item
            invoice_line_item.amount = invoice_line_item.bill_quantity*item.sale_price
            invoice_line_item.tax_amount = invoice_line_item.amount*item.tax.tax_value
            invoice_line_item.total_amount = invoice_line_item.amount+invoice_line_item.tax_amount
            invoice_line_item.save()

        invoice.CalculateTotal()

        return super().form_valid(item_formset)

    def get_success_url(self,*args,**kwargs):
        #delete session data
        del self.request.session['so_invoice_company']
        del self.request.session["so_invoice_saleorder"]
        del self.request.session["so_invoice_selected_item"]

        return reverse('saleorderinvoicesApp:NewSaleOrderInvoice')

class ListSaleOrderInvioce(FormView):
    form_class = SaleOrderInvoiceSearchForm
    template_name = 'saleorderinvoicesApp/list_saleorderinvoice.html'
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['object_list'] = SaleOrderInvoice.objects.all().order_by('invoice_date')
        return context

class DetailSaleOrderInvoice(DetailView):
    model = SaleOrderInvoice
    template_name = 'saleorderinvoicesapp/detailsaleorderinvoice.html'
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['sale_order_items'] = SaleOrderInvoiceItem.objects.filter(sale_order_invoice=self.object)
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
        form.fields.pop('invoice_number')
        form.fields.pop('invoice_date')
        return render(request,'saleorderinvoicesapp/_form_saleorderinvoice1.html',{'form',form})
    if 'so_invoice_company' in request.session:
        initial_selected_company = request.session['so_invoice_company']
        sale_order_id = request.POST.get('sale_order')
        sale_order_item_list = SaleOrderItem.objects.filter(sale_order__id=sale_order_id)
        if sale_order_item_list.exists():
            company_id = str(sale_order_item_list.first().sale_order.supplier.id)
            if initial_selected_company==company_id:
                request.session["so_invoice_saleorder"] = sale_order_id
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
                print("Error SaleOrder Company does not match")
    elif 'so_invoice_company' not in request.session:
        form = SaleOrderInvoiceForm()
        form.fields.pop('invoice_number')
        form.fields.pop('invoice_date')
        return render(request, 'saleorderinvoicesapp/_form_saleorderinvoice1.html',{'form':form})

#AJAX CALL
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
