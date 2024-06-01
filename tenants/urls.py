from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_tenants, name='all_tenants')
]
