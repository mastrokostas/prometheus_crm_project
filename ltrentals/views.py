from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import RentalAgreement, MonthlyPayment
from .forms import AddRentalAgreementForm, EditRentalAgreementForm,TerminateRentalAgreementForm, AddPaymentForm

from properties.models import Property
from tenants.models import Tenant
from users.decorators import allowed_users

# Create your views here.

today = datetime.today()

def get_months_passed(date1,date2):
        delta_months = (date2.year - date1.year) *12 + date2.month - date1.month
        return delta_months

def get_difference(date1,date2):                
        delta_months = (date2.year - date1.year) *12 + date2.month - date1.month
        return delta_months

@login_required(login_url='login')
def all_rental_agreements(request):
    rental_agreements = RentalAgreement.objects.all().order_by('-is_active')
    
    for record in rental_agreements:
        if record.is_active == True:
            #calculate months owed        
            start_date = record.rental_agreement_starting_date
            months_paid = record.months_paid
            months_passed = get_months_passed(start_date,today) +1
            months_still_owed = months_passed - months_paid
            record.months_owed = months_still_owed            
            #calculate expiring
            end_date = record.rental_agreement_ending_date
            expiration = get_difference(today,end_date)
            if expiration <= 6:
                record.expiring = True
            else:
                record.expiring = False
            #save recalculated stuff
            record.save()
    return render(request, 'ltrentals/all_rental_agreements.html', {'rental_agreements':rental_agreements})

@login_required(login_url='login')
def rental_agreement_record(request, pk):
    record = RentalAgreement.objects.get(id=pk)

    #calculate months owed
    if record.is_active == True:        
        start_date = record.rental_agreement_starting_date
        months_paid = record.months_paid
        months_passed = get_months_passed(start_date,today) +1
        months_still_owed = months_passed - months_paid
        record.months_owed = months_still_owed
        record.save()
    #calculate months owed

    months_owed = record.months_owed

    payments = MonthlyPayment.objects.filter(rental_agreement=record.id).order_by('-paid_month')
    form = AddPaymentForm(request.POST or None, initial={'rental_agreement':record.id})
    return render(request, 'ltrentals/rental_agreement_record.html', {'record':record, 'form':form, "payments":payments, "months_owed":months_owed, "today":today})

@login_required(login_url='login')
@allowed_users(allowed_roles=['lt_rentals'])
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
            #calculate total months            
            cleaned_start_date = form.cleaned_data.get('rental_agreement_starting_date')
            cleaned_end_date = form.cleaned_data.get('rental_agreement_ending_date')
            difference=get_difference(cleaned_start_date,cleaned_end_date)
            #make new object and insert total months and months remaining
            new_object = form.save(commit=False)
            new_object.total_months = difference
            new_object.months_remaining = difference
            new_object.save()
            #form.save()
            messages.success(request, "Rental Agreement Added!")
            return redirect('all_rental_agreements')
    return render(request, 'ltrentals/add_rental_agreement.html', {'form':form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['lt_rentals'])
def edit_rental_agreement(request, pk):
    record = RentalAgreement.objects.get(id=pk)
    form = EditRentalAgreementForm(request.POST or None, instance=record)
    if form.is_valid():
        #calculate total months
        cleaned_start_date = form.cleaned_data.get('rental_agreement_starting_date')
        cleaned_end_date = form.cleaned_data.get('rental_agreement_ending_date')
        difference=get_difference(cleaned_start_date,cleaned_end_date)
        #make new object and insert total months and months remaining
        new_object = form.save(commit=False)
        new_object.total_months = difference
        new_object.months_remaining = difference - record.months_paid
        new_object.save()
        #form.save()
        messages.success(request, "Rental Agreement's information has been updated!")
        return redirect('rental_agreement_record', pk=record.pk)
    return render(request, 'ltrentals/edit_rental_agreement.html', {'form': form, 'record': record})

@login_required(login_url='login')
@allowed_users(allowed_roles=['lt_rentals'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['lt_rentals'])
def add_payment(request):
    form = AddPaymentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():            
            rental_agreement = form.cleaned_data.get('rental_agreement')
            #add a month paid & remove a remaining month
            get_object = RentalAgreement.objects.get(id=rental_agreement.id)
            get_object.months_paid += 1
            get_object.months_remaining -=1
            get_object.save()
            form.save()
            messages.success(request, "Payment Added!")
    return redirect('/ltrentals/rental_agreement_record/' + str(rental_agreement.id))
            
    