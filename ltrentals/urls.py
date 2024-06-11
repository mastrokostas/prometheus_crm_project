from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_rental_agreements, name='all_rental_agreements'),
    path('rental_agreement_record/<int:pk>/', views.rental_agreement_record, name='rental_agreement_record'),
    path('add_rental_agreement', views.add_rental_agreement, name='add_rental_agreement'),
    path('edit_rental_agreement/<int:pk>/', views.edit_rental_agreement, name='edit_rental_agreement'),
    path('terminate_rental_agreement/<int:pk>/', views.terminate_rental_agreement, name='terminate_rental_agreement'),
    path('add_payment/', views.add_payment, name='add_payment'),
]