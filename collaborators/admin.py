from django.contrib import admin

from .models import Legal, Electricity, NaturalGas, SubContractor, FurnitureProvider, BuildingManagementCompany

# Register your models here.


class LegalAdmin(admin.ModelAdmin):
    list_display = ("company_name", "company_address",
                    "company_phone", "updated", "created_at")


class ElectricityAdmin(admin.ModelAdmin):
    list_display = ("company_name", "company_address",
                    "company_phone", "updated", "created_at")


class NaturalGasAdmin(admin.ModelAdmin):
    list_display = ("company_name", "company_address",
                    "company_phone", "updated", "created_at")

class SubContractorAdmin(admin.ModelAdmin):
    list_display = ("company_name", "company_address",
                    "company_phone", "updated", "created_at")
    
class FurnitureProviderAdmin(admin.ModelAdmin):
    list_display = ("company_name", "company_address",
                    "company_phone", "updated", "created_at")
    
class BuildingManagementCompanyAdmin(admin.ModelAdmin):
    list_display = ("company_name", "company_address",
                    "company_phone", "updated", "created_at")    


admin.site.register(Electricity, ElectricityAdmin)
admin.site.register(NaturalGas, NaturalGasAdmin)
admin.site.register(Legal, LegalAdmin)
admin.site.register(SubContractor, SubContractorAdmin)
admin.site.register(FurnitureProvider, FurnitureProviderAdmin)
admin.site.register(BuildingManagementCompany,BuildingManagementCompanyAdmin)
