from django.contrib import admin

from .models import Tenant

# Register your models here.

class TenantAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "tax_id",)

admin.site.register(Tenant, TenantAdmin)