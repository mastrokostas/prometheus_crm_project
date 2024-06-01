from django.contrib import admin

from .models import Tenant

# Register your models here.

class TenantAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "is_active", "is_blacklisted",)

admin.site.register(Tenant, TenantAdmin)

admin.site.site_header = "Prometheus Administration"
admin.site.site_title = "CRM Administration"
admin.site.site_title = "CRM Administration"