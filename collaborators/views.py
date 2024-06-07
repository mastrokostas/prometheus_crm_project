from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Legal, Electricity
from .forms import EditLegalForm, EditElectricityForm

# Create your views here.


## Legal

@login_required(login_url='login')
def all_collaborators(request):
    return render(request, "collaborators/all_collaborators.html")

@login_required(login_url='login')
def legal(request):
    lawyers = Legal.objects.all()
    return render(request, "collaborators/legal.html", {"lawyers":lawyers})

@login_required(login_url='login')
def add_legal(request):
    form = EditLegalForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Legal Team Added!")
            return redirect('legal')
    return render(request, 'collaborators/add_legal.html', {'form': form})

@login_required(login_url='login')
def edit_legal(request,pk):
    record = Legal.objects.get(id=pk)
    form = EditLegalForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        messages.success(request, "Legal Team's information has been updated!")
        return redirect('legal')
    return render(request, 'collaborators/edit_legal.html', {'form': form, 'record': record})

# Electricity

@login_required(login_url='login')
def electricity(request):
    companies = Electricity.objects.all()
    return render(request, "collaborators/electricity.html", {"companies":companies})

@login_required(login_url='login')
def add_electricity(request):
    form = EditElectricityForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Electricity Company Added!")
            return redirect('electricity')
    return render(request, 'collaborators/add_electricity.html', {'form': form})

@login_required(login_url='login')
def edit_electricity(request,pk):
    record = Electricity.objects.get(id=pk)
    form = EditElectricityForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        messages.success(request, "Electricity Company's information has been updated!")
        return redirect('electricity')
    return render(request, 'collaborators/edit_electricity.html', {'form': form, 'record': record})