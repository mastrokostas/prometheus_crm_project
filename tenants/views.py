from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from ltrentals.models import RentalAgreement
from .models import Tenant
from .forms import AddTenantForm, EditTenantForm

# Create your views here.


@login_required(login_url='login')
def all_tenants(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenants/all_tenants.html', {'tenants': tenants})


@login_required(login_url='login')
def tenant_record(request, pk):
    record = Tenant.objects.get(id=pk)
    rental_agreements = RentalAgreement.objects.filter(Q(tenant=record.id) | Q(tenant_2=record.id)).order_by('is_active')
    return render(request, 'tenants/tenant_record.html', {'record': record, 'rental_agreements':rental_agreements})


@login_required(login_url='login')
def add_tenant(request):
    form = AddTenantForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Tenant Added!")
            return redirect('all_tenants')
    return render(request, 'tenants/add_tenant.html', {'form': form})


@login_required(login_url='login')
def edit_tenant(request, pk):
    record = Tenant.objects.get(id=pk)
    form = EditTenantForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        messages.success(request, "Tenant's information has been updated!")
        return redirect('tenant_record', pk=record.pk)
    return render(request, 'tenants/edit_tenant.html', {'form': form, 'record': record})
