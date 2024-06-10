from django.contrib import admin

from .models import RentalAgreement

# Register your models here.

class RentalAgreementAdmin(admin.ModelAdmin):
    list_display = ('rental_agreement_name', 'duration', 'owner_file', 'property', 'tenant', 'is_active',)

    def owner_file(self, instance):
        return f"{instance.property.owner_1.file_type}.{instance.property.owner_1.file_number}"
    
    def duration(self, instance):
        return f"{instance.rental_agreement_starting_date} to {instance.rental_agreement_ending_date}"

admin.site.register(RentalAgreement,RentalAgreementAdmin)