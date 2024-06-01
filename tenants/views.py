from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Tenant

# Create your views here.

@login_required(login_url= 'login')
def all_tenants(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenants/all_tenants.html', {'tenants':tenants})

def tenant_record(request,pk):
    record = Tenant.objects.get(id=pk)
    return render (request, 'tenants/tenant_record.html', {'record':record})