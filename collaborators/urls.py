from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_collaborators, name='all_collaborators'),
    path('legal/', views.legal, name='legal'),
    path('edit_legal/<int:pk>/', views.edit_legal, name='edit_legal'),
    path('add_legal/', views.add_legal, name='add_legal'),
    path('electricity/', views.electricity, name='electricity'),
    path('edit_electricity/<int:pk>/', views.edit_electricity, name='edit_electricity'),
    path('add_electricity/', views.add_electricity, name='add_electricity'),
    path('natural_gas/', views.natural_gas, name='natural_gas'),
    path('edit_natural_gas/<int:pk>/', views.edit_natural_gas, name='edit_natural_gas'),
    path('add_natural_gas/', views.add_natural_gas, name='add_natural_gas'),
]