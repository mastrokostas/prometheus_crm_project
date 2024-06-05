from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_landlords, name='all_landlords'),
    path('landlord_record/<int:pk>/', views.landlord_record, name='landlord_record'),
    path('add_landlord/', views.add_landlord, name='add_landlord'),
    path('edit_landlord/<int:pk>/', views.edit_landlord, name='edit_landlord'),
]