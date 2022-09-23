from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone                   ## For the new entry with a startday of NOW

from .models import Project, Category, Entry
from .forms import ProjectForm, CategoryForm, EntryForm


# Create your views here.
class AboutView(TemplateView):
    template_name = "about.html"

class DashboardView(TemplateView):
    template_name = "dashboard_view.html"

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

    ## Found a solution for setting a default date without having to have it on the form.
    ##      start_date is a not-null field, but it can be filled in without entering the form value.
    ##      https://stackoverflow.com/questions/19051830/a-better-way-of-setting-values-in-createview
    def form_valid(self, form):
        obj = form.save(commit=False)
        # obj.user = self.request.user
        obj.start_date = timezone.now()
        obj.save()
        return super().form_valid(form)

class CategoryCreate(SuccessMessageMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')
    success_message = "Category successfully created!"

class CategoryList(ListView):
    model = Category
    template_name= 'category_list.html'

class CategoryUpdate(SuccessMessageMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')
    success_message = "Project successfully updated!"

class CategoryDelete(SuccessMessageMixin, DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category_list')
    success_message = "Category successfully deleted!"

class EntryList(ListView):
    model = Entry
    template_name= 'entry_list.html'

class EntryCreate(SuccessMessageMixin, CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'entry_form.html'
    success_url = reverse_lazy('entry_list')
    success_message = "Entry successfully created!"

class EntryUpdate(SuccessMessageMixin, UpdateView):
    model = Entry
    form_class = EntryForm
    template_name = 'entry_form.html'
    success_url = reverse_lazy('entry_list')
    success_message = "Project successfully updated!"

class EntryDelete(SuccessMessageMixin, DeleteView):
    model = Entry
    template_name = 'entry_confirm_delete.html'
    success_url = reverse_lazy('entry_list')
    success_message = "Entry successfully deleted!"