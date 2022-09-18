from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectList.as_view(), name='project_list'),
    path('view/<int:pk>', views.ProjectDetail.as_view(), name='project_view'),
    path('edit/<int:pk>', views.ProjectUpdate.as_view(), name='project_edit'),
    # path('new', views.ProductCreate.as_view(), name='product_new'),
    # path('delete/<int:pk>', views.ProductDelete.as_view(), name='product_delete'),
]