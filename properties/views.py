from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Property

# Create your views here.

@login_required(login_url='login')
def all_properties(request):
    properties = Property.objects.all()
    return render (request, 'properties/all_properties.html', {'properties':properties})
    
@login_required(login_url='login')
def property_record(request, pk):
    record = Property.objects.get(id=pk)
    return render(request, 'properties/property_record.html', {'record': record})