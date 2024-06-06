from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Property
from .forms import AddPropertyForm, EditPropertyForm

# Create your views here.

@login_required(login_url='login')
def all_properties(request):
    properties = Property.objects.all()
    return render (request, 'properties/all_properties.html', {'properties':properties})
    
@login_required(login_url='login')
def property_record(request, pk):
    record = Property.objects.get(id=pk)
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