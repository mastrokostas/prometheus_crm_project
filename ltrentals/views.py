from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import RentalAgreement
from .forms import AddRentalAgreement

from properties.models import Property

# Create your views here.

@login_required(login_url='login')
def all_rental_agreements(request):
    rental_agreements = RentalAgreement.objects.all()
    return render(request, 'ltrentals/all_rental_agreements.html', {'rental_agreements':rental_agreements})

@login_required(login_url='login')
def rental_agreement_record(request, pk):
    record = RentalAgreement.objects.get(id=pk)
    return render(request, 'ltrentals/rental_agreement_record.html', {'record':record})

def add_rental_agreement(request):
    form = AddRentalAgreement(request.POST or None, initial={'security_deposits':2})
    if request.method == 'POST':
        if form.is_valid():
            #automate utilisation status
            cleaned_property = form.cleaned_data.get('property')
            tracked_property = Property.objects.get(id=cleaned_property.id)
            tracked_property.utilisation_status = "Rented"
            tracked_property.save()
            form.save()
            messages.success(request, "Rental Agreement Added!")
            return redirect('all_rental_agreements')
    return render(request, 'ltrentals/add_rental_agreement.html', {'form':form})