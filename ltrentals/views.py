from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import RentalAgreement

# Create your views here.

@login_required(login_url='login')
def all_rental_agreements(request):
    rental_agreements = RentalAgreement.objects.all()
    return render(request, 'ltrentals/all_rental_agreements.html', {'rental_agreements':rental_agreements})

@login_required(login_url='login')
def rental_agreement_record(request, pk):
    record = RentalAgreement.objects.get(id=pk)
    return render(request, 'ltrentals/rental_agreement_record.html', {'record':record})