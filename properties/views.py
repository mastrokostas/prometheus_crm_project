from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ltrentals.models import RentalAgreement

from .models import Property
from .forms import AddPropertyForm, EditPropertyForm

# Create your views here.
today = datetime.today()

def get_difference(date1,date2):                
        delta_months = (date2.year - date1.year) *12 + date2.month - date1.month
        return delta_months

@login_required(login_url='login')
def all_properties(request):
    properties = Property.objects.all()
    return render (request, 'properties/all_properties.html', {'properties':properties})
    
@login_required(login_url='login')
def property_record(request, pk):
    record = Property.objects.get(id=pk)
    try:
        rental_agreement = RentalAgreement.objects.get(property=record, is_active=True)
        return render(request, 'properties/property_record.html', {'record': record, 'rental_agreement':rental_agreement})
    except:
        return render(request, 'properties/property_record.html', {'record': record})

@login_required(login_url='login')
def add_property(request):
    form = AddPropertyForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Property Added!")
            return redirect('all_properties')
    return render(request, 'properties/add_property.html', {'form': form})

@login_required(login_url='login')
def edit_property(request, pk):
    record = Property.objects.get(id=pk)
    form = EditPropertyForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        messages.success(request, "Property's information has been updated!")
        return redirect('property_record', pk=record.pk)
    return render(request, 'properties/edit_property.html', {'form': form, 'record': record})

@login_required(login_url='login')
def all_rental_guarantees(request):
    properties = Property.objects.filter(under_rental_guarantee=True)
    #calculate RG expiring
    for property in properties:
        #start_date = property.rg_starting
        end_date = property.rg_ending
        if end_date:
            try:            
                expiration = get_difference(today,end_date)
                if expiration <= 6:
                    property.rg_expiring = True
                else:
                    property.rg_expiring = False
                property.save()
            except:
                messages.success(request, "Update Rental Guarantee information for" + property.id)
        else:
            messages.success(request, "Update Rental Guarantee information for property ID: " + str(property.property_id))
    return render(request, 'properties/all_rental_guarantees.html', {"properties":properties})