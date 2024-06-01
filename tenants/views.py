from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Tenant
from .forms import AddTenantForm, EditTenantForm

# Create your views here.

@login_required(login_url= 'login')
def all_tenants(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenants/all_tenants.html', {'tenants':tenants})

@login_required(login_url= 'login')
def tenant_record(request,pk):
    record = Tenant.objects.get(id=pk)
    return render (request, 'tenants/tenant_record.html', {'record':record})

@login_required(login_url= 'login')
def add_tenant(request):
    form = AddTenantForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Tenant Added!")
            return redirect('all_tenants')
    return render(request, 'tenants/add_tenant.html', {'form':form})

@login_required(login_url= 'login')
def edit_tenant(request,pk):
    record = Tenant.objects.get(id=pk)
    form = EditTenantForm(request.POST or None, instance = record)
    if form.is_valid():
        form.save()
        messages.success(request, "Tenant's information has been updated!")
        return redirect ('tenant_record', pk=record.pk)
    return render(request, 'tenants/edit_tenant.html', {'form':form, 'record':record})
