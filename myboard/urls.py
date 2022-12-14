from django.urls import path,include, re_path
from . import views

urlpatterns = [

    # path('', views.DashboardView.as_view()),
    path('', views.get_board),

    ## Project List
    path('list', views.ProjectList.as_view(), name='project_list'),
    path('view/<int:pk>', views.ProjectDetail.as_view(), name='project_view'),
    path('edit/<int:pk>', views.ProjectUpdate.as_view(), name='project_edit'),
    path('delete/<int:pk>', views.ProjectDelete.as_view(), name='project_delete'),
    path('new-project', views.ProjectCreate.as_view(), name='project_new'),

    ## Category List
    path('list-categories', views.CategoryList.as_view(), name='category_list'),
    path('new-category', views.CategoryCreate.as_view(), name='category_new'),
    path('edit-category/<int:pk>', views.CategoryUpdate.as_view(), name='category_edit'),
    path('delete-category/<int:pk>', views.CategoryDelete.as_view(), name='category_delete'),

    ## Entries
    path('list-entries', views.EntryList.as_view(), name='entry_list'),
    path('new-entry', views.EntryCreate.as_view(), name='entry_new'),
    path('edit-entry/<int:pk>', views.EntryUpdate.as_view(), name='entry_edit'),
    path('delete-entry/<int:pk>', views.EntryDelete.as_view(), name='entry_delete'),
]