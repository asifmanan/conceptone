from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from itemsApp.models import Item
from itemsApp.forms import ItemForm, ItemSearchForm
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, FormView

# Create your views here.
class CreateItem(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'itemsapp/create_item.html'
    def get_success_url(self):
        return reverse_lazy('itemsApp:ListItems')

class ListItems(FormView):
    form_class = ItemSearchForm
    template_name = 'itemsapp/list_items.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['object_list'] = Item.objects.all()
        return context

def ItemQuery(request):
    data = request.GET
    query_result = Item.objects.all()
    if data['item_description'] != '':
        query_result = query_result.filter(item_description__icontains=data['item_description'])
    if data['item_type'] != '':
        query_result = query_result.filter(item_type__icontains=data['item_type'])
    if data['item_sub_type'] != '':
        # print(data['po_date'])
        query_result = query_result.filter(item_sub_type__icontains=data['item_sub_type'])
    if data['item_code'] != '':
        query_result = query_result.filter(item_code__icontains=data['item_code'])
    new_html_table = render_to_string('itemsApp/tables/list_itemstable.html',{'object_list':query_result})
    return HttpResponse(new_html_table)
