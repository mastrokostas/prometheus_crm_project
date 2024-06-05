from django.contrib import admin

from .models import Landlord

# Register your models here.

class LandlordAdmin(admin.ModelAdmin):
    list_display = ("file_number", "last_name", "first_name", "nationality", "is_active", "updated", "created_at")

admin.site.register(Landlord,LandlordAdmin)