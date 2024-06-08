from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Legal, Electricity, NaturalGas, BuildingManagementCompany, SubContractor, FurnitureProvider
from .forms import EditLegalForm, EditElectricityForm, EditNaturalGasForm, EditBuildingManagerForm, EditSubContractorForm, EditFurnitureProviderForm

# Create your views here.

# All
@login_required(login_url='login')
def all_collaborators(request):
    return render(request, "collaborators/all_collaborators.html")


## Legal
@login_required(login_url='login')
def legal(request):
    lawyers = Legal.objects.all()
    return render(request, "collaborators/legal.html", {"lawyers":lawyers})

@login_required(login_url='login')
def edit_legal(request,pk):
    record = Legal.objects.get(id=pk)
    form = EditLegalForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        messages.success(request, "Legal Team's information has been updated!")
        return redirect('legal')
    return render(request, 'collaborators/edit_legal.html', {'form': form, 'record': record})

@login_required(login_url='login')
def add_legal(request):
    form = EditLegalForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Legal Team Added!")
            return redirect('legal')
    return render(request, 'collaborators/add_legal.html', {'form': form})


## Electricity
@login_required(login_url='login')
def electricity(request):
    companies = Electricity.objects.all()
    return render(request, "collaborators/electricity.html", {"companies":companies})

@login_required(login_url='login')
def edit_electricity(request,pk):
    record = Electricity.objects.get(id=pk)
    form = EditElectricityForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        messages.success(request, "Electricity Company's information has been updated!")
        return redirect('electricity')
    return render(request, 'collaborators/edit_electricity.html', {'form': form, 'record': record})

@login_required(login_url='login')
def add_electricity(request):
    form = EditElectricityForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Electricity Company Added!")
            return redirect('electricity')
    return render(request, 'collaborators/add_electricity.html', {'form': form})


## Natural Gas
@login_required(login_url='login')
def natural_gas(request):
    companies = NaturalGas.objects.all()
    return render(request, "collaborators/natural_gas.html", {"companies":companies})

@login_required(login_url='login')
def edit_natural_gas(request,pk):
    record = NaturalGas.objects.get(id=pk)
    form = EditNaturalGasForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        messages.success(request, "Natural Gas Company's information has been updated!")
        return redirect('natural_gas')
    return render(request, 'collaborators/edit_natural_gas.html', {'form': form, 'record': record})

@login_required(login_url='login')
def add_natural_gas(request):
    form = EditNaturalGasForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Natural Gas Company Added!")
            return redirect('natural_gas')
    return render(request, 'collaborators/add_natural_gas.html', {'form': form})


## Building Managers
@login_required(login_url='login')
def building_managers(request):
    companies = BuildingManagementCompany.objects.all()
    return render(request, "collaborators/building_managers.html", {"companies":companies})

def edit_building_manager(request,pk):
    record = BuildingManagementCompany.objects.get(id=pk)
    form = EditBuildingManagerForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        messages.success(request, "Building Management Company's information has been updated!")
        return redirect('building_managers')
    return render(request, 'collaborators/edit_building_manager.html', {'form': form, 'record': record})

@login_required(login_url='login')
def add_building_manager(request):
    form = EditBuildingManagerForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Building Management Company Added!")
            return redirect('building_managers')
    return render(request, 'collaborators/add_building_manager.html', {'form': form})


## Sub-Contractors
@login_required(login_url='login')
def sub_contractors(request):
    companies = SubContractor.objects.all()
    return render(request, "collaborators/sub_contractors.html", {"companies":companies})

def edit_sub_contractor(request,pk):    
    record = SubContractor.objects.get(id=pk)
    form = EditSubContractorForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        messages.success(request, "Sub-Contractor's information has been updated!")
        return redirect('sub_contractors')
    return render(request, 'collaborators/edit_sub_contractor.html', {'form': form, 'record': record})

@login_required(login_url='login')
def add_sub_contractor(request):
    form = EditSubContractorForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Sub-Contractor Added!")
            return redirect('sub_contractors')
    return render(request, 'collaborators/add_sub_contractor.html', {'form': form})


## Furniture Providers
@login_required(login_url='login')
def furniture_providers(request):
    companies = FurnitureProvider.objects.all()
    return render(request, "collaborators/furniture_providers.html", {"companies":companies})

def edit_furniture_provider(request,pk):    
    record = FurnitureProvider.objects.get(id=pk)
    form = EditFurnitureProviderForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        messages.success(request, "Furniture Provider's information has been updated!")
        return redirect('furniture_providers')
    return render(request, 'collaborators/edit_furniture_provider.html', {'form': form, 'record': record})

@login_required(login_url='login')
def add_furniture_provider(request):
    form = EditFurnitureProviderForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Furniture Provider Added!")
            return redirect('furniture_providers')
    return render(request, 'collaborators/add_furniture_provider.html', {'form': form})