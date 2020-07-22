from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.generic import (
                                CreateView,
                                DeleteView,
                                FormView,
                                )

from saleordersApp.models import SaleOrder, SaleOrderItem
from saleordersApp.forms import (
                                SaleOrderForm,
                                SaleOrderItemForm,
                                SaleOrderSearchForm,
                                )
# Create your views here.
class CreateSaleOrder(CreateView):
    model = SaleOrder
    form_class = SaleOrderForm
    template_name = 'saleordersapp/create_saleorder.html'
    def get_success_url(self):
        return reverse_lazy('saleordersApp:CreateSaleOrderItem',kwargs={'pk':self.object.pk})

class CreateSaleOrderItem(CreateView):
    model = SaleOrderItem
    form_class = SaleOrderItemForm
    template_name = 'saleordersapp/create_saleorderitem.html'
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        saleorder = SaleOrder.objects.get(pk=self.kwargs['pk'])
        # saleorder.CalculateSaleOrderTotal()
        line_items = SaleOrderItem.objects.filter(sale_order=saleorder)
        context['saleorder'] = saleorder
        context['object_list'] = line_items
        return context

    def form_valid(self,form):
        if form.is_valid():
            line_item = form.save(commit=False)
            line_item.sale_order = get_object_or_404(SaleOrder,pk=self.kwargs['pk'])
            current_obj = SaleOrderItem.objects.filter(sale_order=line_item.sale_order).order_by('-line_number').first()
            if current_obj != None:
                new_line_number = (current_obj.line_number) + 1
            else:
                new_line_number = 1
            line_item.line_number = new_line_number
            line_item.amount = line_item.sale_price*line_item.order_quantity
            line_item.tax_amount = line_item.amount*line_item.tax.tax_value
            line_item.total_amount = line_item.amount+line_item.tax_amount
            line_item.save()
            line_item.add_amount_to_saleorder()
            return super(CreateSaleOrder,self).form_valid(form)
        else:
            print("in form in-valid")
            return super(CreateSaleOrder,self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('saleordersApp:CreateSaleOrderItem',kwargs={'pk':self.object.sale_order.pk})

class DeleteSaleOrderItem(DeleteView):
    model = SaleOrderItem
    def get_success_url(self):
        saleorder = self.object.sale_order
        obj_pk = self.object.id
        line_items = SaleOrderItem.objects.filter(sale_order = saleorder)
        proceeding_line_items = line_items.filter(line_number__gt=self.object.line_number)
        if proceeding_line_items.exists():
            i = self.object.line_number
            for item in proceeding_line_items:
                item.line_number = i
                item.save()
                i = i + 1
        self.object.remove_amount_from_saleorder()
        return reverse_lazy('saleordersApp:CreateSaleOrderItem',kwargs={'pk':saleorder.id})

class ListSaleOrder(FormView):
    form_class = SaleOrderSearchForm
    template_name = 'saleordersapp/list_saleorder.html'
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['object_list'] = SaleOrder.objects.all().order_by('so_date')
        return context

def SaleOrderQuery(request):
    data = request.GET
    query_result = SaleOrder.objects.all()
    if data['so_number'] != '':
        query_result = query_result.filter(so_number__icontains=data['so_number'])
    if data['buyer'] != '':
        query_result = query_result.filter(buyer__customer_name__icontains=data['buyer'])
    if data['buyer_po_number'] != '':
        query_result = query_result.filter(buyer_po_number__icontains=data['buyer_po_number'])
    if data['buyer_po_date'] != '':
        query_result = query_result.filter(buyer_po_date__range=[(data['buyer_po_date']),(data['buyer_po_date'])])
    new_html_table = render_to_string('saleordersApp/tables/list_saleordertable.html',{'object_list':query_result})
    return HttpResponse(new_html_table)
