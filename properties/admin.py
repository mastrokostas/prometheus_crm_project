from django.contrib import admin

from .models import Property

# Register your models here.

class PropertytAdmin(admin.ModelAdmin):
    list_display = ("property_id", "address", "municipality", "updated", "created_at")


admin.site.register(Property,PropertytAdmin)