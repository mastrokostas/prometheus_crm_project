from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_properties, name='all_properties'),
    path('property_record/<int:pk>/', views.property_record, name='property_record'),
]