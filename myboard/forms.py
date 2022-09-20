# -*- coding: utf-8 -*-
from django import forms

from .models import Project, Category

class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['project_name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['project_description'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['isactive'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }

    class Meta:
        model = Project
        fields = ('project_name', 'project_description', 'isactive')

class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['category_name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['category_description'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['isactive'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }

    class Meta:
        model = Category
        fields = ('category_name', 'category_description', 'isactive')