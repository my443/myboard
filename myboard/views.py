from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Project
from .forms import ProjectForm


# Create your views here.
class AboutView(TemplateView):
    template_name = "about.html"

class ProjectList(ListView):
    model = Project
    template_name= 'project_list.html'

class ProjectDetail(DetailView):
    model = Project
    template_name = 'edit_project.html'

class ProjectUpdate(SuccessMessageMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project_form.html'
    success_url = reverse_lazy('project_list')
    success_message = "Product successfully updated!"


