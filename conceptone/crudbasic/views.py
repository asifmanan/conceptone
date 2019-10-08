from django.shortcuts import render, redirect
from crudbasic.models import Customers, Suppliers, Projects, Items
from crudbasic.forms import CustomerForm, SupplierForm, ProjectForm, ItemForm, BasicSearch
from django.utils import translation
from django.views.generic import View, TemplateView, ListView, DetailView
from crudbasic.basic_functions import get_col_heads

# Create your views here.
class IndexView(TemplateView):
    template_name = 'crudbasic/index.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context ['page_title'] = ''
        return context

class BaseDisplayView(TemplateView):
    template_name = 'crudbasic/customers.html'
    if 'customers' in request.path:
        main_title = 'Customers'
        create_link = 'Create New Customer'
        model = Customers

    def get(self, request, *args, **kwargs):
        search_form = BasicSearch(caller = model)
        page_data = model.objects.order_by('created_on')
        return render(request, self.template_name, {'page_data': page_data,'search_form' : search_form})

    def post(self, request, *args, **kwargs):
        search_form = BasicSearch(request.POST, caller = model)
        if search_form.is_valid():
            data = request.POST.copy()
            qby = data.get('search_by')
            qstrting = data.get('search_for')
            queryparam = qby+'__'+'contains'
            search_list = model.objects.filter(**{queryparam:qstrting})
            page_data = search_list
        else:
            search_form = BasicSearch(caller = model)
            page_data = model.objects.order_by('created_on')
            return render(request, self.template_name, {'page_data': page_data,'search_form' : search_form})
        return render(request, self.template_name, {'page_data': page_data,'search_form':search_form})


class CustomerView(ListView):
    template_name = 'crudbasic/customers.html'
    model = Customers
    context_object_name = 'customer_data'

    def get(self, request, *args, **kwargs):
        search_form = BasicSearch(caller = Customers)
        customer_data = Customers.objects.order_by('created_on')
        return render(request, self.template_name, {'customer_data': customer_data,'search_form' : search_form})

    def post(self, request, *args, **kwargs):
        search_form = BasicSearch(request.POST, caller = Customers)
        if search_form.is_valid():
            data = request.POST.copy()
            qby = data.get('search_by')
            qstrting = data.get('search_for')
            queryparam = qby+'__'+'contains'
            search_list = Customers.objects.filter(**{queryparam:qstrting})
            customer_data = search_list
        else:
            search_form = BasicSearch(caller = Customers)
            customer_data = Customers.objects.order_by('customer_name')
            return render(request, self.template_name, {'customer_data': customer_data,'search_form' : search_form})
        return render(request, self.template_name, {'customer_data': customer_data,'search_form':search_form})

class SupplierView(TemplateView):
    template_name = 'crudbasic/suppliers.html'
    model = Suppliers
    context_object_name = 'supplier_data'

    def get(self, request, *args, **kwargs):
        search_form = BasicSearch(caller = Suppliers)
        supplier_data = Suppliers.objects.order_by('created_on')
        return render(request, self.template_name, {'supplier_data': supplier_data,'search_form' : search_form})

    def post(self, request, *args, **kwargs):
        search_form = BasicSearch(request.POST, caller = Suppliers)
        if search_form.is_valid():
            data = request.POST.copy()
            qby = data.get('search_by')
            qstrting = data.get('search_for')
            queryparam = qby+'__'+'contains'
            search_list = Suppliers.objects.filter(**{queryparam:qstrting})
            supplier_data = search_list
        else:
            search_form = BasicSearch(caller = Suppliers)
            supplier_data = Suppliers.objects.order_by('supplier_name')
            return render(request, self.template_name, {'supplier_data': supplier_data,'search_form' : search_form})
        return render(request, self.template_name, {'supplier_data': supplier_data,'search_form':search_form})

# def index(request):
#     return render(request,"crudbasic/index.html")

# def customers(request):
#     customers_list = Customers.objects.order_by('customer_name')
#     form = CustomerForm()
#     # id = "cu"
#     search_form = BasicSearch()
#
#     if request.method == 'POST':
#         if 'search' in request.POST:
#             search_form = BasicSearch(request.POST)
#             if search_form.is_valid():
#                 data = request.POST.copy()
#                 # print(data)
#                 qby = data.get('search_by')
#                 qstring = data.get('search_for')
#                 queryparam = qby+'__'+'contains'
#                 # search_list = Customers.objects.filter(customer_name__contains=q)
#                 search_list = Customers.objects.filter(**{ queryparam:qstring })
#                 customers_list = search_list
#
#     translation.activate('en')
#     return render(request,"crudbasic/customers.html",{'form':form,'search_form':search_form,'customer_data':customers_list})

def CreateCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if 'save' in request.POST:
            if form.is_valid():
                form.save(commit=True)
                return redirect('crudbasic:customers')
            else:
                print("ERROR! Form is invalid")

        if 'save-addnew' in request.POST:
            if form.is_valid():
                form.save(commit=True)
                form = CustomerForm()
                return render(request,'crudbasic/CreateCustomer.html',{'form':form})
            else:
                print("ERROR! Form is invalid")
    translation.activate('en')
    return render(request,"crudbasic/CreateCustomer.html",{'form':form})

def CreateSupplier(request):
    form = SupplierForm()
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if 'save' in request.POST:
            if form.is_valid():
                form.save(commit=True)
                return redirect('crudbasic:suppliers')
            else:
                print("ERROR! Form is invalid")

        if 'save-addnew' in request.POST:
            if form.is_valid():
                form.save(commit=True)
                form = CustomerForm()
                return render(request,'crudbasic/createsustomer.html',{'form':form})
            else:
                print("ERROR! Form is invalid")
    translation.activate('en')
    return render(request,"crudbasic/createsupplier.html",{'form':form})

def suppliers(request):
    suppliers_list = Suppliers.objects.order_by('supplier_name')
    form = SupplierForm()
    search_form = BasicSearch()
    if request.method == 'POST':
        if 'search' in request.POST:
            data = request.POST.copy()
            # print(data)
            q = data.get('search_for')
            search_list = Supplier.objects.filter(supplier_name__contains=q)
            supplier_list = search_list
        if 'save' in request.POST:
            form = SupplierForm(request.POST)
            if form.is_valid:
                form.save(commit=True)
                return redirect('crudbasic:suppliers')
            else:
                print("ERROR! Form is invalid")
    translation.activate('en')
    return render(request,"crudbasic/suppliers.html",{'form':form,'search_form':search_form,'supplier_data':suppliers_list})

def projects(request):
    projects_list = Projects.objects.order_by('project_name')
    form = ProjectForm()
    search_form = BasicSearch()
    if request.method == 'POST':
        if 'search' in request.POST:
            data = request.POST.copy()
            q = data.get('search_for')
            search_list = Projects.objects.filter(project_name__contains=q)
            projects_list = search_list
        if 'save' in request.POST:
            form = ProjectForm(request.POST)
            if form.is_valid:
                form.save(commit=True)
                return redirect('crudbasic:projects')
            else:
                print("ERROR! Form is invalid")
    return render(request,"crudbasic/projects.html",{'form':form,'search_form':search_form,'project_data':projects_list})

def CreateProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if 'save' in request.POST:
            if form.is_valid():
                form.save(commit=True)
                return redirect('crudbasic:projects')
            else:
                print("ERROR! Form is invalid")

        if 'save-addnew' in request.POST:
            if form.is_valid():
                form.save(commit=True)
                form = ProjectForm()
                return render(request,'crudbasic/createproject.html',{'form':form})
            else:
                print("ERROR! Form is invalid")
    translation.activate('en')
    return render(request,"crudbasic/createproject.html",{'form':form})

def items(request):
    item_list = Items.objects.order_by('item_line')
    form = ItemForm()
    search_form = BasicSearch()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid:
            form.save(commit=True)
            return redirect('crudbasic:items')
        else:
            print("ERROR! Form is invalid")
    return render(request,"crudbasic/items.html", {'form':form, 'search_form':search_form,'item_data':item_list})

def CreateItem(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if 'save' in request.POST:
            if form.is_valid():
                form.save(commit=True)
                return redirect('crudbasic:items')
            else:
                print("ERROR! Form is invalid")

        if 'save-addnew' in request.POST:
            if form.is_valid():
                form.save(commit=True)
                form = ItemForm()
                return render(request,'crudbasic/createitem.html',{'form':form})
            else:
                print("ERROR! Form is invalid")
    translation.activate('en')
    return render(request,"crudbasic/createitem.html",{'form':form})
