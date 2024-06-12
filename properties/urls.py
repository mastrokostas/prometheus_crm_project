from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_properties, name='all_properties'),
    path('property_record/<int:pk>/', views.property_record, name='property_record'),
    path('add_property/', views.add_property, name='add_property'),
    path('edit_property/<int:pk>/', views.edit_property, name='edit_property'),
    path('all_rental_guarantees/', views.all_rental_guarantees, name='all_rental_guarantees')
]