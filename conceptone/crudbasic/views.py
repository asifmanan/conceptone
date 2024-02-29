from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.forms.formsets import formset_factory

from django.http import FileResponse

from crudbasic.models import (
                                Projects,
                                TaxRate,
                            )
from crudbasic.forms import (
                                ProjectForm,
                                TaxRateForm,
                                BasicSearch,
                            )
from django.utils import translation
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from crudbasic.basic_functions import get_col_heads, printpo2pdf, generatePdf

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

class CreateTaxRateView(CreateView):
    model = TaxRate
    form_class = TaxRateForm
    template_name='crudbasic/createtax.html'

    def get_success_url(self):
        if 'save-addnew' in self.request.POST:
            return reverse('crudbasic:createtax')
        else:
            return reverse('crudbasic:index')

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

class UpdateProjectView(UpdateView):
    model = Projects
    form_class = ProjectForm
    template_name = 'crudbasic/createproject.html'

    def get_success_url(self):
        return reverse('crudbasic:projects')


#######################
####   DeleteViews  ###
#######################

class DeleteTaxRateView(DeleteView):
    model = TaxRate
    success_url = reverse_lazy('crudbasic:taxrates')
    template_name = 'crudbasic/dialog/objdelconf.html'

class DeleteProjectView(DeleteView):
    model = Projects
    success_url = reverse_lazy('crudbasic:projects')
    template_name = 'crudbasic/dialog/objdelconf.html'
