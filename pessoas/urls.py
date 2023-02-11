from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_alias'),
    path('home', views.home, name='home_alias'),
    path('pacientes', views.pacientes.as_view(), name='pacientes_alias'),
    path('procedimentos', views.procedimentos.as_view(), name='procedimentos_alias'),
    path('pessoa_create/', views.pessoa_create.as_view(), name='pessoa_create_alias'),
    path('pessoa_update/<int:pk>/', views.pessoa_update.as_view(), name='pessoa_update_alias'),
    path('pessoa_delete/<int:pk>/', views.pessoa_delete.as_view(), name='pessoa_delete_alias'),
    path('pessoa_download/', views.pessoa_download, name='pessoa_download_alias'),
    path('procedimento_update/<int:pk>/', views.procedimento_update.as_view(), name='procedimento_update_alias'),
    path('procedimento_delete/<int:pk>/', views.procedimento_delete.as_view(), name='procedimento_delete_alias'),
    path('procedimento_create/', views.procedimento_create.as_view(), name='procedimento_create_alias'),
    path('procedimento_download/', views.procedimento_download, name='procedimento_download_alias'),
]