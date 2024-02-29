from django.shortcuts import render
# from django.template.loader import render_to_string
from django.http import HttpResponse
from projectsApp.models import Project
from projectsApp.forms import ProjectForm, ProjectSearchForm
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, FormView
# Create your views here.
class CreateProject(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projectsApp/create_project.html'
    def get_success_url(self):
        return reverse_lazy('projectsApp:ListProjects')

class ListProjects(FormView):
    form_class = ProjectSearchForm
    template_name = 'projectsapp/list_projects.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['object_list'] = Project.objects.all()
        return context
