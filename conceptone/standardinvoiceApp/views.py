from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, FormView

from standardinvoiceApp.models import StandardInvoice, StandardInvoiceItem
from standardinvoiceApp.forms import StandardInvoiceForm, StandardInvoiceItemForm
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
        context['invoice'] = inv
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
        # line_item.purchase_order.CalculateSoTotal()
        return super().form_valid(form)
