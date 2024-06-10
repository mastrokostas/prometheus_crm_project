from itertools import count
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import RentalAgreement
from .forms import AddRentalAgreementForm, EditRentalAgreementForm,TerminateRentalAgreementForm

from properties.models import Property
from tenants.models import Tenant

# Create your views here.

@login_required(login_url='login')
def all_rental_agreements(request):
    rental_agreements = RentalAgreement.objects.all()
    return render(request, 'ltrentals/all_rental_agreements.html', {'rental_agreements':rental_agreements})

@login_required(login_url='login')
def rental_agreement_record(request, pk):
    record = RentalAgreement.objects.get(id=pk)
    return render(request, 'ltrentals/rental_agreement_record.html', {'record':record})

@login_required(login_url='login')
def add_rental_agreement(request):
    form = AddRentalAgreementForm(request.POST or None, initial={'security_deposits':2})
    if request.method == 'POST':
        if form.is_valid():
            #automate utilisation status
            cleaned_property = form.cleaned_data.get('property')
            tracked_property = Property.objects.get(id=cleaned_property.id)
            tracked_property.utilisation_status = "Rented"
            tracked_property.save()
            #automate tenant activity
            cleaned_tenant = form.cleaned_data.get('tenant')
            tracked_tenant = Tenant.objects.get(id=cleaned_tenant.id)
            try:
                cleaned_tenant_2 = form.cleaned_data.get('tenant_2')
                tracked_tenant_2 = Tenant.objects.get(id=cleaned_tenant_2.id)
            except:
                tracked_tenant.is_active = True
                tracked_tenant.save()
            else:
                tracked_tenant.is_active = True
                tracked_tenant.save()
                tracked_tenant_2.is_active = True
                tracked_tenant_2.save()
            form.save()
            messages.success(request, "Rental Agreement Added!")
            return redirect('all_rental_agreements')
    return render(request, 'ltrentals/add_rental_agreement.html', {'form':form})

@login_required(login_url='login')
def edit_rental_agreement(request, pk):
    record = RentalAgreement.objects.get(id=pk)
    form = EditRentalAgreementForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        messages.success(request, "Rental Agreement's information has been updated!")
        return redirect('rental_agreement_record', pk=record.pk)
    return render(request, 'ltrentals/edit_rental_agreement.html', {'form': form, 'record': record})

@login_required(login_url='login')
def terminate_rental_agreement(request,pk):
    record = RentalAgreement.objects.get(id=pk)
    selected_property = Property.objects.get(id=record.property.id)
    form = TerminateRentalAgreementForm(request.POST or None, instance=record)
    if form.is_valid():
        selected_property.utilisation_status = "Vacant"        
        record.is_active = False       
        #automate tenant deactivation        
        tracked_tenant = Tenant.objects.get(id=record.tenant.id)
        ra_count = RentalAgreement.objects.filter(Q(tenant=tracked_tenant) | Q(tenant_2=tracked_tenant)).filter(is_active=True).count()
        try:
            tracked_tenant_2 = Tenant.objects.get(id=record.tenant_2.id)
            ra_count_2 = RentalAgreement.objects.filter(Q(tenant=tracked_tenant_2) | Q(tenant_2=tracked_tenant_2)).filter(is_active=True).count()
        except:
            if ra_count == 1:
                tracked_tenant.is_active = False
                tracked_tenant.save()
        else:
            if ra_count == 1:
                tracked_tenant.is_active = False
                tracked_tenant.save()            
            if ra_count_2 == 1:
                tracked_tenant_2.is_active = False
                tracked_tenant_2.save()
        form.save()
        record.save()
        selected_property.save()           
        messages.success(request, "Rental Agreement has been terminated!")
        return redirect('rental_agreement_record', pk=record.pk)
    return render(request, 'ltrentals/terminate_rental_agreement.html', {'form': form, 'record': record})