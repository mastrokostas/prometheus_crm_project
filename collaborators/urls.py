from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_collaborators, name='all_collaborators'),
    path('legal/', views.legal, name='legal'),
    path('edit_legal/<int:pk>/', views.edit_legal, name='edit_legal'),
    path('add_legal/', views.add_legal, name='add_legal'),
]