from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_tenants, name='all_tenants'),
    path('tenant_record/<int:pk>', views.tenant_record, name='tenant_record'),
    path('add_tenant/', views.add_tenant, name='add_tenant'),
    path('edit_tenant/<int:pk>', views.edit_tenant, name='edit_tenant'),
]
