from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse, reverse_lazy
from django.utils import timezone
import datetime
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                CreateView, UpdateView, DetailView, FormView,
                                DeleteView,)
from purchaseApp.models import PurchaseOrder, PurchaseOrderItem
from crudbasic.models import Suppliers
from purchaseApp.forms import PurchaseOrderForm, PurchaseOrderItemForm,PurchaseOrderSearchForm
# Create your views here.
# class CreatePurchaseOrder():
class CreatePurchaseOrder(CreateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = 'purchaseapp/createpurchaseorder.html'
    def get_success_url(self):
        return reverse_lazy('purchaseApp:CreatePurchaseOrderItems',kwargs={'pk':self.object.pk})

class CreatePurchaseOrderItems(FormView):
    form_class = PurchaseOrderItemForm
    template_name = 'purchaseapp/createpurchaseorderitems.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        self.po_object = PurchaseOrder.objects.get(pk=self.kwargs['pk'])
        context['po_object'] = self.po_object
        context['order_items'] = PurchaseOrderItem.objects.filter(purchase_order=self.po_object)
        print(self.po_object)
        self.po_object.CalculatePoTotal()
        return context

    def form_valid(self,form):
        line_item = form.save(commit=False)
        line_item.purchase_order = get_object_or_404(PurchaseOrder, pk=self.kwargs['pk'])
        current_obj = PurchaseOrderItem.objects.filter(purchase_order=line_item.purchase_order).order_by('-po_line_number').first()
        if current_obj !=None:
            new_line_number = (current_obj.po_line_number) + 1
        else:
            new_line_number = 1
        line_item.po_line_number = new_line_number
        line_item.total_price = line_item.purchase_price*line_item.order_quantity
        line_item.save()
        # line_item.purchase_order.CalculateSoTotal()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('purchaseApp:CreatePurchaseOrderItems',kwargs={'pk':self.kwargs['pk']})

class ListPurchaseOrders(FormView):
    form_class = PurchaseOrderSearchForm
    template_name = 'purchaseapp/list_purchaseorders.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['object_list'] = PurchaseOrder.objects.all()
        return context
#AJAX View
def PurchaseOrderQuery(request):
    data = request.GET
    query_result = PurchaseOrder.objects.all()
    if data['supplier'] != '':
        query_result = query_result.filter(supplier__supplier_name__icontains=data['supplier'])
    if data['project'] != '':
        query_result = query_result.filter(project__project_name__icontains=data['project'])
    if data['po_date'] != '':
        print(data['po_date'])
        query_result = query_result.filter(po_date__range=[(data['po_date']),(data['po_date'])])
    if data['po_number'] != '':
        query_result = query_result.filter(po_number__icontains=data['po_number'])
    new_html_table = render_to_string('purchaseApp/tables/list_purchaseorderstable.html',{'object_list':query_result})
    return HttpResponse(new_html_table)

class DeletePurchaseOrder(DeleteView):
    model = PurchaseOrder
    success_url = reverse_lazy('purchaseApp:ListPurchaseOrders')
    template_name = 'purchaseapp/deletepoconfirmation.html'

class DeletePurchaseOrderItem(DeleteView):
    model = PurchaseOrderItem
    # success_url = reverse_lazy('PurchaseApp:CreatePurchaseOrderItems')
    def get_success_url(self):
        po_object = self.object.purchase_order
        obj_pk=self.object.id
        line_items = PurchaseOrderItem.objects.filter(purchase_order=po_object)
        proceeding_line_items = line_items.filter(po_line_number__gt=self.object.po_line_number)
        if proceeding_line_items.exists():
            i = self.object.po_line_number
            for item in proceeding_line_items:
                item.po_line_number = i
                item.save()
                i = i + 1
        # print(proceeding_line_items)
        # print(obj.id)
        return reverse_lazy('purchaseApp:CreatePurchaseOrderItems', kwargs={'pk':po_object.id})

class PublishPoConfirmation(UpdateView):
    model = PurchaseOrder
    form_class=PurchaseOrderForm
    template_name = 'purchaseapp/publish_po_confirmation.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['object']=self.object
        print(self.object.pk)
        return context

    def form_valid(self, form):
        # self.object = PurchaseOrder.objects.filter(pk=self.kwargs.pk)
        if form.is_valid():
            print(self.object.project.po_date)
        return super().form_valid(form)
    def get_success_url(self):
        print(self.object.project.project_name)
        return reverse_lazy('purchaseApp:ListPurchaseOrders')


def PoPublishConfirmation(request,pk):
    po_object = get_object_or_404(PurchaseOrder,pk=pk)
    object_list = PurchaseOrderItem.objects.filter(po_number=po_object).order_by('po_line_number')
    if request.method == 'POST':
        if 'proceed' in request.POST:
            po_object.publish()
            print(po_obj.po_publish)
            print(timezone.now())
            print("PO PUBLISDHED SUCCESSFULLY!")
            return render(request,'purchaseapp/publishedpoview.html',{'po_object':po_object})
    return render(request,'purchaseapp/publish_po_conf.html',{'po_object':po_object})


#####################################################
class Published_PoView(DetailView):
    model = PurchaseOrderItem
    def get_queryset(self):
        return
    # def get(self, request, *args, **kwargs):
    #     main_title = ''


class OrderItemView(ListView):
    model = PurchaseOrderItem
    template_name = 'crudbasic/basedisplay.html'
    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_data'] = PurchaseOrderItem.objects.order_by('created_on')
        # context['search_form'] = BasicSearch(caller = OrderItem)
        table_head_temp = get_col_heads(PurchaseOrderItem)
        table_head = []
        for idx, val in enumerate(table_head_temp):
            table_head.append(str(val[1]).split(" ")[1])

        context['table_head'] = table_head
        context['main_title'] = 'Purchase Orders (Items)'
        context['create_link'] = create_link= {'name':'Create New PO','value':'crudbasic:newpurchaseorder'}
        return context



    # def form_valid(self, form):
    #     self.kwargs['po_amount'] = 0.00
    #     return super(CreatePurchaseOrder, self).form_valid(form)

def PublishedPoView(request,pk):
    po_obj = get_object_or_404(PurchaseOrder,pk=pk)
    page_data = PurchaseOrderItem.objects.filter(po_number=po_obj).order_by('po_line_number')
    return render(request,'crudbasic/PublishedPoView.html',{'po_obj':po_obj,'page_data':page_data})

def PrintPurchaseOrder(request,pk):
    po_obj = get_object_or_404(PurchaseOrder,pk=pk)
    po_lines = PurchaseOrderItem.objects.filter(po_number=po_obj).order_by('po_line_number')
    # buffer = printpo2pdf(po_obj, po_lines)
    buffer = generatePdf(po_obj,po_lines)
    return FileResponse(buffer,as_attachment=False,filename="hello.pdf")

#ajax call view
def loaditemrates(request):
    if request.GET.get('item') == "":
        data = 0.0
        return JsonResponse({'data':data})
    item_id = request.GET.get('item')
    print(item_id)
    selected_item = Items.objects.get(pk=item_id)
    data = selected_item.item_price
    # print(data)
    #return render(request, 'crudbasic/ajaxhtml/loaditemrates.html',{'item_ra':item_ra})
    return JsonResponse({'data':data})

def CreateOrderItem(request,pk):
    po_obj = get_object_or_404(PurchaseOrder,pk=pk)
    po_num = po_obj.po_number
    po_obj.CalculatePoTotal()
    # print(po_obj.po_amount)
    page_data = PurchaseOrderItem.objects.filter(po_number=po_obj).order_by('po_line_number')
    if po_obj.po_publish == True:
        return render(request,'crudbasic/PublishedPoView.html',{'po_obj':po_obj,'page_data':page_data})
    form = PurchaseOrderItemForm()
    if request.method=='POST':
        form = PurchaseOrderItemForm(request.POST)
        if form.is_valid():
            itemline = form.save(commit=False)
            itemline.po_number = po_obj
            # po_obj.po_amount = po_obj.CalculatePoTotal()
            # new_line_number = (len(OrderItem.objects.filter(po_number=po_obj)))+1
            current_obj = PurchaseOrderItem.objects.filter(po_number=po_obj).order_by('-po_line_number').first()
            # print(current_obj)
            if current_obj !=None:
                new_line_number = (current_obj.po_line_number) + 1
            else:
                new_line_number = 1
            # new_line_number = current_line_num + 1
            # max_line = max(temp_obj.aggregate(max('po_line_number'))
            itemline.po_line_number = new_line_number
            itemline.total_price = itemline.purchase_price*itemline.order_quantity
            itemline.save()
            po_obj.CalculatePoTotal()
        else:
            print("An Error Occured")
    else:
        form = PurchaseOrderItemForm()
    return render(request,'crudbasic/poadditems.html',{'form':form,'po_obj':po_obj,'page_data':page_data})

class UpdatePurchaseOrder(UpdateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = 'crudbasic/newpurchase.html'

    def get_success_url(self):
        if'save' in self.request.POST:
            return reverse_lazy('crudbasic:purchaseorders')
        if'continue' in self.request.POST:
            return reverse_lazy('crudbasic:poadditems',kwargs={'pk':self.object.pk})

class DeletePurchaseOrderView(DeleteView):
    model = PurchaseOrder
    success_url = reverse_lazy('crudbasic:purchaseorders')
    template_name = 'crudbasic/dialog/objdelconf.html'
