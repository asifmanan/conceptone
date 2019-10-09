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
        context['page_title'] = ''
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
            search_form = BasicSearch(caller = Customers)
            main_title = 'Customers'
            create_link = 'Create New Customer'
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
