from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from properties.models import Property
from landlords.models import Landlord
from tenants.models import Tenant
from collaborators.models import Legal, Electricity, NaturalGas, SubContractor, FurnitureProvider, BuildingManagementCompany

# Create your views here.

@login_required(login_url='login')
def search(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        #print(searched)
        properties = Property.objects.filter(Q(property_id__contains=searched) | Q(address__contains=searched) | Q(utilisation__contains=searched) | Q(utilisation_status__contains=searched))
        landlords = Landlord.objects.filter(Q(file_number__contains=searched) | Q(first_name__contains=searched) | Q(last_name__contains=searched) | Q(tax_id__contains=searched) |Q(passport_number__contains=searched))
        tenants = Tenant.objects.filter(Q(first_name__contains=searched) | Q(last_name__contains=searched) | Q(phone__contains=searched) | Q(phone_2__contains=searched) | Q(tax_id__contains=searched))
        legals = Legal.objects.filter(Q(company_name__contains=searched) | Q(company_phone__contains=searched))
        electricity_companies = Electricity.objects.filter(Q(company_name__contains=searched))
        lng_companies = NaturalGas.objects.filter(Q(company_name__contains=searched))
        sub_contractors = SubContractor.objects.filter(Q(company_name__contains=searched))
        furniture_providers = FurnitureProvider.objects.filter(Q(company_name__contains=searched))
        management_companies = BuildingManagementCompany.objects.filter(Q(company_name__contains=searched))
        #print("aaa", legals)
        return render(request, 'search/search.html', {"searched":searched, "properties":properties, "landlords":landlords, "tenants":tenants, "legals":legals, "electricity_companies":electricity_companies, "lng_companies":lng_companies, "sub_contractors":sub_contractors, "furniture_providers":furniture_providers, "management_companies":management_companies})
    else:
        return render(request, 'search/search.html', {})