from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from django.http import HttpResponse

from django.views.generic import CreateView, ListView, FormView, DeleteView

from standardinvoiceApp.models import StandardInvoice, StandardInvoiceItem
from standardinvoiceApp.forms import (
                                        StandardInvoiceForm,
                                        StandardInvoiceItemForm,
                                        StandardInvoiceSearchForm,
                                        )
# Create your views here.
class CreateStandardInvoice(CreateView):
    model = StandardInvoice
    form_class = StandardInvoiceForm
    template_name = 'standardinvoiceapp/create_standardinvoice.html'
    def get_success_url(self):
        return reverse_lazy('standardinvoiceApp:CreateStandardInvoiceItem',kwargs={'pk':self.object.pk})

class CreateStandardInvoiceItem(CreateView):
    model = StandardInvoiceItem
    form_class = StandardInvoiceItemForm
    template_name = 'standardinvoiceapp/create_standardinvoiceitem.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        inv = StandardInvoice.objects.get(pk=self.kwargs['pk'])
        line_items = StandardInvoiceItem.objects.filter(invoice=inv)
        context['invoice'] = inv
        context['object_list'] = line_items
        return context
    def form_valid(self,form):
        line_item = form.save(commit=False)
        line_item.invoice = get_object_or_404(StandardInvoice,pk=self.kwargs['pk'])
        current_obj = StandardInvoiceItem.objects.filter(invoice=line_item.invoice).order_by('-line_number').first()
        if current_obj !=None:
            new_line_number = (current_obj.line_number) + 1
        else:
            new_line_number = 1
        line_item.line_number = new_line_number
        line_item.total_price = line_item.sale_price*line_item.quantity
        line_item.tax_amount = line_item.total_price*line_item.tax.tax_value
        line_item.total_amount = line_item.total_price+line_item.tax_amount
        line_item.save()
        line_item.add_amount_to_invoice()
        # line_item.invoice.CalculateInvoiceTotal()
        # line_item.purchase_order.CalculateSoTotal()
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('standardinvoiceApp:CreateStandardInvoiceItem',kwargs={'pk':self.object.invoice.pk})

class DeleteStandardInvoiceItem(DeleteView):
    model = StandardInvoiceItem
    def get_success_url(self):
        invoice = self.object.invoice
        obj_pk = self.object.id
        line_items = StandardInvoiceItem.objects.filter(invoice=invoice)
        proceeding_line_items = line_items.filter(line_number__gt=self.object.line_number)
        if proceeding_line_items.exists():
            i = self.object.line_number
            for item in proceeding_line_items:
                item.line_number = i
                item.save()
                i = i + 1
        self.object.remove_amount_from_invoice()
        return reverse_lazy('standardinvoiceApp:CreateStandardInvoiceItem', kwargs={'pk':invoice.id})

class ListStandardInvoice(FormView):
    form_class = StandardInvoiceSearchForm
    template_name = 'standardinvoiceapp/list_standardinvoice.html'
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['object_list'] = StandardInvoice.objects.all().order_by('invoice_date')
        return context

def StandardInvoiceQuery(request):
    data = request.GET
    query_result = StandardInvoice.objects.all()
    if data['invoice_number'] != '':
        query_result = query_result.filter(invoice_number__icontains=data['invoice_number'])
    if data['customer'] != '':
        query_result = query_result.filter(customer__customer_name__icontains=data['customer'])
    if data['project'] != '':
        query_result = query_result.filter(project__project_name__icontains=data['project'])
    if data['invoice_date'] != '':
        print(data['invoice_date'])
        query_result = query_result.filter(invoice_date__range=[(data['invoice_date']),(data['invoice_date'])])
    new_html_table = render_to_string('standardinvoiceApp/tables/list_standardinvoicetable.html',{'object_list':query_result})
    return HttpResponse(new_html_table)
