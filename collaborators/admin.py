from django.contrib import admin

from .models import Legal

# Register your models here.

class LegalAdmin(admin.ModelAdmin):
    list_display = ("company_name", "company_address", "company_phone", "updated", "created_at")

admin.site.register(Legal, LegalAdmin)