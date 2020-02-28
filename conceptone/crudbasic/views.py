from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.forms.formsets import formset_factory
from crudbasic.models import (
                                Customers,
                                Suppliers,
                                Projects,
                                Items,
                                TaxRate,
                                PurchaseOrder,
                                OrderItem,
                            )
from crudbasic.forms import (
                                CustomerForm,
                                SupplierForm,
                                ProjectForm,
                                ItemForm,
                                TaxRateForm,
                                BasicSearch,
                                PurchaseOrderForm,
                                OrderItemForm,

                            )
from django.utils import translation
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from crudbasic.basic_functions import get_col_heads

# Create your views here.
class IndexView(TemplateView):
    template_name = 'crudbasic/index.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = ''
        return context

class TaxRateView(ListView):
    model = TaxRate
    template_name='crudbasic/basedisplay.html'

    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_data'] = TaxRate.objects.order_by('created_on')

        table_head_temp = get_col_heads(TaxRate)
        table_head = []
        for idx, val in enumerate(table_head_temp):
            table_head.append(str(val[1]).split(" ")[1])

        context['table_head'] = table_head
        context['main_title'] = 'Tax Rates'
        context['create_link'] = create_link= {'name':'Define New Tax','value':'crudbasic:createtax'}
        return context

class PurchaseOrderView(ListView):
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

class CustomerView(TemplateView):
    template_name = 'crudbasic/basedisplay.html'
    def get(self, request, *args, **kwargs):
        main_title = 'Customers'
        create_link= {'name':'Create New Customer','value':'crudbasic:createcustomer'}
        search_form = BasicSearch(caller = Customers)
        table_head_temp = get_col_heads(Customers)
        table_head = []
        for idx, val in enumerate(table_head_temp):
            table_head.append(str(val[1]).split(" ")[1])
        page_data = Customers.objects.order_by('created_on')
        return render(request, self.template_name, {'page_data': page_data,
                                                    'search_form' : search_form,
                                                    'table_head':table_head,
                                                    'main_title':main_title,
                                                    'create_link':create_link
                                                    })

    def post(self, request, *args, **kwargs):
        search_form = BasicSearch(request.POST, caller = Customers)
        if search_form.is_valid():
            data = request.POST.copy()
            qby = data.get('search_by')
            qstrting = data.get('search_for')
            queryparam = qby+'__'+'contains'
            search_list = Customers.objects.filter(**{queryparam:qstrting})

            main_title = 'Customers'
            create_link= {'name':'Create New Customer','value':'crudbasic:createcustomer'}
            table_head_temp = get_col_heads(Customers)
            table_head = []
            for idx, val in enumerate(table_head_temp):
                table_head.append(str(val[1]).split(" ")[1])
            page_data = search_list
        else:
            search_form = BasicSearch(request.POST, caller = Customers)
            main_title = 'Customers'
            create_link = {'name':'Create New Customer','value':'crudbasic:createcustomer'}
            table_head = None
            page_data = None
        return render(request, self.template_name, {'page_data': page_data,
                                                    'search_form' : search_form,
                                                    'table_head':table_head,
                                                    'main_title':main_title,
                                                    'create_link':create_link
                                                    })

class SupplierView(TemplateView):
    template_name = 'crudbasic/basedisplay.html'
    def get(self, request, *args, **kwargs):
        main_title = 'Suppliers'
        create_link= {'name':'Create New Supplier','value':'crudbasic:createsupplier'}
        search_form = BasicSearch(caller = Suppliers)
        table_head_temp = get_col_heads(Suppliers)
        table_head = []
        for idx, val in enumerate(table_head_temp):
            table_head.append(str(val[1]).split(" ")[1])
        page_data = Suppliers.objects.order_by('created_on')
        return render(request, self.template_name, {'page_data': page_data,
                                                    'search_form' : search_form,
                                                    'table_head':table_head,
                                                    'main_title':main_title,
                                                    'create_link':create_link
                                                    })
    def post(self, request, *args, **kwargs):
        search_form = BasicSearch(request.POST, caller = Suppliers)
        if search_form.is_valid():
            data = request.POST.copy()
            qby = data.get('search_by')
            qstrting = data.get('search_for')
            queryparam = qby+'__'+'contains'
            search_list = Suppliers.objects.filter(**{queryparam:qstrting})

            main_title = 'Suppliers'
            create_link= {'name':'Create New Supplier','value':'crudbasic:createsupplier'}
            table_head_temp = get_col_heads(Suppliers)
            table_head = []
            for idx, val in enumerate(table_head_temp):
                table_head.append(str(val[1]).split(" ")[1])
            page_data = search_list
        else:
            search_form = BasicSearch(caller = Suppliers)
            main_title = 'Suppliers'
            create_link= {'name':'Create New Supplier','value':'crudbasic:createsupplier'}
            table_head = None
            page_data = None
        return render(request, self.template_name, {'page_data': page_data,
                                                    'search_form' : search_form,
                                                    'table_head':table_head,
                                                    'main_title':main_title,
                                                    'create_link':create_link
                                                    })

class ProjectView(TemplateView):
    template_name = 'crudbasic/basedisplay.html'
    def get(self, request, *args, **kwargs):
        main_title = 'Projects'
        create_link= {'name':'Create New Project','value':'crudbasic:createproject'}
        search_form = BasicSearch(caller = Projects)
        table_head_temp = get_col_heads(Projects)
        table_head = []
        for idx, val in enumerate(table_head_temp):
            table_head.append(str(val[1]).split(" ")[1])
        page_data = Projects.objects.order_by('created_on')
        return render(request, self.template_name, {'page_data': page_data,
                                                    'search_form' : search_form,
                                                    'table_head':table_head,
                                                    'main_title':main_title,
                                                    'create_link':create_link
                                                    })
    def post(self, request, *args, **kwargs):
        search_form = BasicSearch(request.POST, caller = Projects)
        if search_form.is_valid():
            data = request.POST.copy()
            qby = data.get('search_by')
            qstrting = data.get('search_for')
            queryparam = qby+'__'+'contains'
            search_list = Projects.objects.filter(**{queryparam:qstrting})

            main_title = 'Projects'
            create_link= {'name':'Create New Project','value':'crudbasic:createproject'}
            table_head_temp = get_col_heads(Projects)
            table_head = []
            for idx, val in enumerate(table_head_temp):
                table_head.append(str(val[1]).split(" ")[1])
            page_data = search_list
        else:
            search_form = BasicSearch(caller = Projects)
            main_title = 'Projects'
            create_link= {'name':'Create New Project','value':'crudbasic:createproject'}
            table_head = None
            page_data = None
        return render(request, self.template_name, {'page_data': page_data,
                                                    'search_form' : search_form,
                                                    'table_head':table_head,
                                                    'main_title':main_title,
                                                    'create_link':create_link
                                                    })

class ItemView(TemplateView):
    template_name = 'crudbasic/basedisplay.html'
    def get(self, request, *args, **kwargs):
        main_title = 'Items'
        create_link= {'name':'Create New Item','value':'crudbasic:createitem'}
        search_form = BasicSearch(caller = Items)
        table_head_temp = get_col_heads(Items)
        table_head = []
        for idx, val in enumerate(table_head_temp):
            table_head.append(str(val[1]).split(" ")[1])
        page_data = Items.objects.order_by('created_on')
        return render(request, self.template_name, {'page_data': page_data,
                                                    'search_form' : search_form,
                                                    'table_head':table_head,
                                                    'main_title':main_title,
                                                    'create_link':create_link
                                                    })
    def post(self, request, *args, **kwargs):
        search_form = BasicSearch(request.POST, caller = Items)
        if search_form.is_valid():
            data = request.POST.copy()
            qby = data.get('search_by')
            qstrting = data.get('search_for')
            queryparam = qby+'__'+'contains'
            search_list = Items.objects.filter(**{queryparam:qstrting})

            main_title = 'Items'
            create_link= {'name':'Create New Item','value':'crudbasic:createitem'}
            table_head_temp = get_col_heads(Items)
            table_head = []
            for idx, val in enumerate(table_head_temp):
                table_head.append(str(val[1]).split(" ")[1])
            page_data = search_list
        else:
            search_form = BasicSearch(caller = Items)
            main_title = 'Items'
            create_link= {'name':'Create New Item','value':'crudbasic:createitem'}
            table_head = None
            page_data = None
        return render(request, self.template_name, {'page_data': page_data,
                                                    'search_form' : search_form,
                                                    'table_head':table_head,
                                                    'main_title':main_title,
                                                    'create_link':create_link
                                                    })

#######################
####   CreateViews  ###
#######################

# class CreateOrderItem(CreateView):
#     model = OrderItem
#     form_class = OrderItemForm
#     template_name = 'crudbasic/neworderitems.html'

def CreateOrderItem(request,pk):
    po_obj = get_object_or_404(PurchaseOrder,pk=pk)
    po_num = po_obj.po_number
    # po_num_int = cast(po_num,output_field = IntegerField())
    # print(po_num_int)
    page_data = OrderItem.objects.filter(po_number=po_obj).order_by('po_line_number')
    form = OrderItemForm()
    if request.method=='POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            itemline = form.save(commit=False)
            itemline.po_number = po_obj
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
        else:
            print("An Error Occured")
    else:
        form = OrderItemForm()
    return render(request,'crudbasic/neworderitems.html',{'form':form,'po_obj':po_obj,'page_data':page_data})
    #
    # def get_context_data(self, **kwargs):
    #     po_obj = get_object_or_404(PurchaseOrder,pk=pk)
    # if request.method=='POST':
    #     form = OrderItemForm(request.POST)
    #     if form.is_valid():
    #         itemline = form.save(commit=False)
    #         itemline.po_number = po_obj
    #         itemline.total_price = itemline.purchase_price*itemline.order_quantity
    #         itemline.save()
    #     else:
    #         form = OrderItemForm()
    # def get_success_url(self):
    #     if'save' in self.request.POST:
    #         return reverse_lazy('crudbasic:purchaseorders')
    #     if'continue' in self.request.POST:
    #         return reverse_lazy('crudbasic:neworderitems',kwargs={'pk':self.object.pk})
    # return render(request,'crudbasic/neworderitems.html',{'formset':form,'po_obj':po_obj})

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

class CreatePurchaseOrder(CreateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = 'crudbasic/newpurchase.html'

    def get_success_url(self):
        if'save' in self.request.POST:
            return reverse_lazy('crudbasic:purchaseorders')
        if'continue' in self.request.POST:
            return reverse_lazy('crudbasic:neworderitems',kwargs={'pk':self.object.pk})

    # def form_valid(self, form):
    #     self.kwargs['po_amount'] = 0.00
    #     return super(CreatePurchaseOrder, self).form_valid(form)

class CreateTaxRateView(CreateView):
    model = TaxRate
    form_class = TaxRateForm
    template_name='crudbasic/createtax.html'

    def get_success_url(self):
        if 'save-addnew' in self.request.POST:
            return reverse('crudbasic:createtax')
        else:
            return reverse('crudbasic:index')

class CreateCustomerView(CreateView):
    # fields = '__all__'
    # if defining form_class then fields cannot be used
    model = Customers
    form_class = CustomerForm
    template_name = 'crudbasic/createcustomer.html'

    def get_success_url(self):
        if 'save-addnew' in self.request.POST:
            return reverse('crudbasic:createcustomer')
        else:
            return reverse('crudbasic:customers')

class CreateSupplierView(CreateView):
    model = Suppliers
    form_class = SupplierForm
    template_name = 'crudbasic/createsupplier.html'

    def get_success_url(self):
        if 'save-addnew' in self.request.POST:
            return reverse('crudbasic:createsupplier')
        if 'save' in self.request.POST:
            return reverse('crudbasic:suppliers')

class CreateItemView(CreateView):
    model = Items
    form_class = ItemForm
    template_name = 'crudbasic/createitem.html'

    def get_success_url(self):
        if 'save-addnew' in self.request.POST:
            return reverse('crudbasic:createitem')
        if 'save' in self.request.POST:
            return reverse('crudbasic:items')

class CreateProjectView(CreateView):
    model = Projects
    form_class = ProjectForm
    template_name = 'crudbasic/createproject.html'

    def get_success_url(self):
        if 'save-addnew' in self.request.POST:
            return reverse('crudbasic:createproject')
        if 'save' in self.request.POST:
            return reverse('crudbasic:projects')

#######################
####   UpdateViews  ###
#######################

class UpdateTaxRateView(UpdateView):
    model = TaxRate
    form_class = TaxRateForm
    template_name = 'crudbasic/createtax.html'

    def get_success_url(self):
        return reverse('crudbasic:taxrates')

class UpdateCustomerView(UpdateView):
    model = Customers
    form_class = CustomerForm
    template_name = 'crudbasic/createcustomer.html'

    def get_success_url(self):
        return reverse('crudbasic:customers')

class UpdateSupplierView(UpdateView):
    model = Suppliers
    form_class = SupplierForm
    template_name = 'crudbasic/createsupplier.html'

    def get_success_url(self):
        return reverse('crudbasic:suppliers')

class UpdateItemView(UpdateView):
    model = Items
    form_class = ItemForm
    template_name = 'crudbasic/createitem.html'

    def get_success_url(self):
        return reverse('crudbasic:items')

class UpdateProjectView(UpdateView):
    model = Projects
    form_class = ProjectForm
    template_name = 'crudbasic/createproject.html'

    def get_success_url(self):
        return reverse('crudbasic:projects')

class UpdatePurchaseOrder(UpdateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = 'crudbasic/newpurchase.html'

    def get_success_url(self):
        if'save' in self.request.POST:
            return reverse_lazy('crudbasic:purchaseorders')
        if'continue' in self.request.POST:
            return reverse_lazy('crudbasic:neworderitems',kwargs={'pk':self.object.pk})

# class UpdateOrderItemView(UpdateView):
#     model = OrderItem
#     form_class = OrderItemForm
#     template_name = 'crudbasic/orderitemupdate.html'

#######################
####   DeleteViews  ###
#######################

class DeleteTaxRateView(DeleteView):
    model = TaxRate
    success_url = reverse_lazy('crudbasic:taxrates')
    template_name = 'crudbasic/dialog/objdelconf.html'

class DeleteCustomerView(DeleteView):
    model = Customers
    success_url = reverse_lazy('crudbasic:customers')
    template_name = 'crudbasic/dialog/objdelconf.html'

class DeleteSupplierView(DeleteView):
    model = Suppliers
    success_url = reverse_lazy('crudbasic:suppliers')
    template_name = 'crudbasic/dialog/objdelconf.html'

class DeleteItemView(DeleteView):
    model = Items
    success_url = reverse_lazy('crudbasic:items')
    template_name = 'crudbasic/dialog/objdelconf.html'

class DeleteProjectView(DeleteView):
    model = Projects
    success_url = reverse_lazy('crudbasic:projects')
    template_name = 'crudbasic/dialog/objdelconf.html'

class DeletePurchaseOrderView(DeleteView):
    model = PurchaseOrder
    success_url = reverse_lazy('crudbasic:purchaseorders')
    template_name = 'crudbasic/dialog/objdelconf.html'
