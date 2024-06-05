from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Landlord
from .forms import AddLandlordForm, EditLandlordForm

# Create your views here.


@login_required(login_url='login')
def all_landlords(request):
    landlords = Landlord.objects.all().order_by('file_type').order_by('file_number')
    return render(request, 'landlords/all_landlords.html', {'landlords': landlords})


@login_required(login_url='login')
def landlord_record(request, pk):
    record = Landlord.objects.get(id=pk)
    return render(request, 'landlords/landlord_record.html', {'record': record})


@login_required(login_url='login')
def add_landlord(request):
    form = AddLandlordForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Landlord Added!")
            return redirect('all_landlords')
    return render(request, 'landlords/add_landlord.html', {'form': form})


@login_required(login_url='login')
def edit_landlord(request, pk):
    record = Landlord.objects.get(id=pk)
    form = EditLandlordForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        messages.success(request, "Landlord's information has been updated!")
        return redirect('landlord_record', pk=record.pk)
    return render(request, 'landlords/edit_landlord.html', {'form': form, 'record': record})
