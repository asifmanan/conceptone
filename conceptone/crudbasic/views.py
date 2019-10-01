from django.shortcuts import render, redirect
from crudbasic.models import Customers, Suppliers, Projects, Items
from crudbasic.forms import CustomerForm, SupplierForm, ProjectForm, ItemForm, BasicSearch
from django.utils import translation
from crudbasic.basic_functions import get_col_heads

# Create your views here.
def index(request):
    return render(request,"crudbasic/index.html")

def customers(request):
    customers_list = Customers.objects.order_by('customer_name')
    form = CustomerForm()
    search_form = BasicSearch()

    if request.method == 'POST':
        if 'search' in request.POST:
            data = request.POST.copy()
            # print(data)
            qby = data.get('search_by')
            qstring = data.get('search_for')
            queryparam = qby+'__'+'contains'
            # search_list = Customers.objects.filter(customer_name__contains=q)
            search_list = Customers.objects.filter(**{ queryparam:qstring })
            customers_list = search_list
        if 'save' in request.POST:
            form = CustomerForm(request.POST)
            if form.is_valid:
                form.save(commit=True)
                return redirect('crudbasic:customers')
            else:
                print("ERROR! Form is invalid")
    translation.activate('en')
    return render(request,"crudbasic/customers1.html",{'form':form,'search_form':search_form,'customer_data':customers_list})

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

def items(request):
    item_list = Items.objects.order_by('item_line')
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid:
            form.save(commit=True)
            return redirect('crudbasic:items')
        else:
            print("ERROR! Form is invalid")
    return render(request,"crudbasic/items.html", {'form':form,'item_data':item_list})
