from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone                   ## For the new entry with a startday of NOW

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
    success_message = "Project successfully updated!"

class ProjectDelete(SuccessMessageMixin, DeleteView):
    model = Project
    template_name = 'project_confirm_delete.html'
    success_url = reverse_lazy('project_list')
    success_message = "Project successfully deleted!"

class ProjectCreate(SuccessMessageMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project_form.html'
    success_url = reverse_lazy('project_list')
    success_message = "Project successfully created!"

    def form_valid(self, form):
        obj = form.save(commit=False)
        # obj.user = self.request.user
        obj.start_date = timezone.now()
        obj.save()
        return super().form_valid(form)


