from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                CreateView, UpdateView, DetailView, FormView,
                                DeleteView,)
from purchaseApp.models import PurchaseOrder, OrderItem
from purchaseApp.forms import PurchaseOrderForm, OrderItemForm
# Create your views here.
# class CreatePurchaseOrder():
class CreatePurchaseOrder(CreateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = 'purchaseapp/createpurchaseorder.html'

    def get_success_url(self):
        if'save' in self.request.POST:
            return reverse_lazy('crudbasic:purchaseorders')
        if'continue' in self.request.POST:
            return reverse_lazy('crudbasic:poadditems',kwargs={'pk':self.object.pk})


class ViewPurchaseOrdersList(ListView):
    model = PurchaseOrder
    template_name = 'crudbasic/basedisplay.html'

    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_data'] = PurchaseOrder.objects.order_by('created_on')
        context['search_form'] = BasicSearch(caller = PurchaseOrder)
        table_head_temp = get_col_heads(PurchaseOrder)
        table_head = []
        for idx, val in enumerate(table_head_temp):
            table_head.append(str(val[1]).split(" ")[1])

        context['table_head'] = table_head
        context['main_title'] = 'Purchase Orders'
        context['create_link'] = create_link= {'name':'Create New PO','value':'crudbasic:newpurchaseorder'}
        return context
    def post(self, request, *args, **kwargs):
        search_form = BasicSearch(request.POST, caller = PurchaseOrder)
        if search_form.is_valid():
            data = request.POST.copy()
            qby = data.get('search_by')
            qstrting = data.get('search_for')
            queryparam = qby+'__'+'contains'
            search_list = PurchaseOrder.objects.filter(**{queryparam:qstrting})

            main_title = 'Purchase Orders'
            create_link= {'name':'Create New PO','value':'crudbasic:newpurchaseorder'}
            table_head_temp = get_col_heads(PurchaseOrder)
            table_head = []
            for idx, val in enumerate(table_head_temp):
                table_head.append(str(val[1]).split(" ")[1])
            page_data = search_list
        else:
            search_form = BasicSearch(request.POST, caller = PurchaseOrder)
            main_title = 'Purchase Orders'
            create_link = {'name':'Create New PO','value':'crudbasic:newpurchaseorder'}
            table_head = None
            page_data = None
        return render(request, self.template_name, {'page_data': page_data,
                                                    'search_form' : search_form,
                                                    'table_head':table_head,
                                                    'main_title':main_title,
                                                    'create_link':create_link
                                                    })

class Published_PoView(DetailView):
    model = OrderItem
    def get_queryset(self):
        return
    # def get(self, request, *args, **kwargs):
    #     main_title = ''


class OrderItemView(ListView):
    model = OrderItem
    template_name = 'crudbasic/basedisplay.html'
    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_data'] = OrderItem.objects.order_by('created_on')
        # context['search_form'] = BasicSearch(caller = OrderItem)
        table_head_temp = get_col_heads(OrderItem)
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
    page_data = OrderItem.objects.filter(po_number=po_obj).order_by('po_line_number')
    return render(request,'crudbasic/PublishedPoView.html',{'po_obj':po_obj,'page_data':page_data})

def PoPublishConfirmation(request,pk):
    po_obj = get_object_or_404(PurchaseOrder,pk=pk)
    page_data = OrderItem.objects.filter(po_number=po_obj).order_by('po_line_number')
    if request.method == 'POST':
        if 'proceed' in request.POST:
            po_obj.publish()
            print(po_obj.po_publish)
            print(timezone.now())
            print("PO PUBLISDHED SUCCESSFULLY!")
            return render(request,'crudbasic/publishedpoview.html',{'po_obj':po_obj,'page_data':page_data})
    return render(request,'crudbasic/publishpoconf.html',{'po_obj':po_obj})

def PrintPurchaseOrder(request,pk):
    po_obj = get_object_or_404(PurchaseOrder,pk=pk)
    po_lines = OrderItem.objects.filter(po_number=po_obj).order_by('po_line_number')
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
    page_data = OrderItem.objects.filter(po_number=po_obj).order_by('po_line_number')
    if po_obj.po_publish == True:
        return render(request,'crudbasic/PublishedPoView.html',{'po_obj':po_obj,'page_data':page_data})
    form = OrderItemForm()
    if request.method=='POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            itemline = form.save(commit=False)
            itemline.po_number = po_obj
            # po_obj.po_amount = po_obj.CalculatePoTotal()
            # new_line_number = (len(OrderItem.objects.filter(po_number=po_obj)))+1
            current_obj = OrderItem.objects.filter(po_number=po_obj).order_by('-po_line_number').first()
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
        form = OrderItemForm()
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
