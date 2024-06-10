from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_rental_agreements, name='all_rental_agreements'),
    path('rental_agreement_record/<int:pk>/', views.rental_agreement_record, name='rental_agreement_record'),
]