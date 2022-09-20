from django.urls import path
from . import views

urlpatterns = [

    ## Project List
    path('', views.ProjectList.as_view(), name='project_list'),
    path('view/<int:pk>', views.ProjectDetail.as_view(), name='project_view'),
    path('edit/<int:pk>', views.ProjectUpdate.as_view(), name='project_edit'),
    path('delete/<int:pk>', views.ProjectDelete.as_view(), name='project_delete'),
    path('new-project', views.ProjectCreate.as_view(), name='project_new'),

    ## Category List
    path('new-category', views.CategoryCreate.as_view(), name='category_new'),
]