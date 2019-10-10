from django.shortcuts import render, redirect
from django.urls import reverse
from crudbasic.models import Customers, Suppliers, Projects, Items
from crudbasic.forms import CustomerForm, SupplierForm, ProjectForm, ItemForm, BasicSearch
from django.utils import translation
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView
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

class UpdateCustomerView(UpdateView):
    model = Customers
    form_class = CustomerForm
    template_name = 'crudbasic/createcustomer.html'

    def get_success_url(self):
        return reverse('crudbasic:createcustomer')
        
class CreateSupplierView(CreateView):
    model = Suppliers
    form_class = SupplierForm
    template_name = 'crudbasic/createsupplier.html'

    def get_success_url(self):
        if 'save-addnew' in self.request.POST:
            return reverse('crudbasic:createsupplier')
        if 'save' in self.request.POST:
            return reverse('crudbasic:suppliers')

class CreateProjectView(CreateView):
    model = Projects
    form_class = ProjectForm
    template_name = 'crudbasic/createproject.html'

    def get_success_url(self):
        if 'save-addnew' in self.request.POST:
            return reverse('crudbasic:createproject')
        if 'save' in self.request.POST:
            return reverse('crudbasic:projects')

class CreateItemView(CreateView):
    model = Items
    form_class = ItemForm
    template_name = 'crudbasic/createitem.html'

    def get_success_url(self):
        if 'save-addnew' in self.request.POST:
            return reverse('crudbasic:createitem')
        if 'save' in self.request.POST:
            return reverse('crudbasic:items')
