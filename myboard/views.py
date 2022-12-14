from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone                   ## For the new entry with a startday of NOW

from django.shortcuts import render
from django.http import HttpResponse, request

from django.db.models import DecimalField
from django.db.models import Sum, Avg

from .models import Project, Category, Entry
from .forms import ProjectForm, CategoryForm, EntryForm

import datetime

# Create your views here.
class AboutView(TemplateView):
    template_name = "about.html"

def get_board1(request):
    # model = Entry

    year = request.GET.get('year', '')
    return HttpResponse(year)

def get_board(request):
    # model = Entry

    current_date = datetime.datetime.today()
    current_year = current_date.year
    current_month = current_date.month

    # Use request.GET.get to get the parametre from the url /?year=2022
    # year = request.GET.get('year', '')
    # year = request.POST.get('year', '')

    # Either get the posted year or the current year.
    year = request.POST.get('year', str(current_year))

    # You have to use getlist if you are selecting more than one item
    month = request.POST.getlist('month')

    # If there is no month selected, selected the current month.
    if not month:
        month = [str(current_month)]

    print ('Month', month)

    possible_years = ['2021', '2022', '2023', '2024', '2025', '2026', '2027']

    available_hours     = Entry.objects.filter(category__exact = 7).aggregate(Sum('hours'))
    billable_hours      = Entry.objects.filter(category__exact=8).aggregate(Sum('hours'))
    bid_hours           = Entry.objects.filter(category__exact=9).aggregate(Sum('hours'))

    billable_revenue    = Entry.objects.filter(category__exact=8).aggregate(Sum('dollars'))
    bid_revenue         = Entry.objects.filter(category__exact=8).aggregate(Sum('dollars'))

    firm_hours          = Entry.objects.filter(category__exact=10).aggregate(Sum('hours'))
    outsourced_hours    = Entry.objects.filter(category__exact=11).aggregate(Sum('hours'))

    context = {
                     'available_hours'  : available_hours['hours__sum'],
                     'billable_hours'   : billable_hours['hours__sum'],
                     'bid_hours'        : bid_hours['hours__sum'],
                     'billable_revenue' : "{:,}".format(billable_revenue['dollars__sum']),
                     'bid_revenue'      : bid_revenue['dollars__sum'],
                     'firm_hours'       : firm_hours['hours__sum'],
                     'outsourced_hours' : outsourced_hours['hours__sum'],
                     'year'             : year,
                     'possible_years'   : possible_years,
                     'month'            : month}

    return render(request, 'dashboard_view.html', context)

class DashboardView(TemplateView):
    model = Entry
    year = ''

    template_name = "dashboard_view.html"


    available_hours = Entry.objects.filter(category__exact = 7).aggregate(Sum('hours'))
    billable_hours = Entry.objects.filter(category__exact=8).aggregate(Sum('hours'))
    bid_hours = Entry.objects.filter(category__exact=9).aggregate(Sum('hours'))

    billable_revenue = Entry.objects.filter(category__exact=8).aggregate(Sum('dollars'))
    bid_revenue = Entry.objects.filter(category__exact=8).aggregate(Sum('dollars'))

    firm_hours = Entry.objects.filter(category__exact=10).aggregate(Sum('hours'))
    outsourced_hours = Entry.objects.filter(category__exact=11).aggregate(Sum('hours'))

    def dispatch(self, request, *args, **kwargs):
        year = request.GET.get('year', '')
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     context['year'] = self.year
    #     return context

    extra_context = {
                     'available_hours' : available_hours['hours__sum'],
                     'billable_hours' : billable_hours['hours__sum'],
                     'bid_hours' : bid_hours['hours__sum'],
                     'billable_revenue' : "{:,}".format(billable_revenue['dollars__sum']),
                     'bid_revenue' : bid_revenue['dollars__sum'],
                     'firm_hours' : firm_hours['hours__sum'],
                     'outsourced_hours' : outsourced_hours['hours__sum'],
                     'year'             : year}


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