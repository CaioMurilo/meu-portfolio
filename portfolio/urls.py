from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projetos/', views.projects_list, name='projects_list'), # NOVA LINHA
    path('pagina/<slug:slug>/', views.page_detail, name='page_detail'),
    path('projeto/<slug:slug>/', views.project_detail, name='project_detail'),
]