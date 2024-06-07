from django.contrib import admin

from .models import Legal, Electricity, NaturalGas

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


admin.site.register(Electricity, ElectricityAdmin)
admin.site.register(NaturalGas, NaturalGasAdmin)
admin.site.register(Legal, LegalAdmin)
