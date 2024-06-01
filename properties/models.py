from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class Property(models.Model):

    class ProgressChoices(models.TextChoices):
        completed = "Completed"
        in_progress = "In Progress"
        not_started_yet = "Not Started Yet"

    class FurnitureChoices(models.TextChoices):
        full = "Fully furnished"
        partial = "Semi - furnished"
        no_furniture = "No Furniture"

    class UtilisationChoices(models.TextChoices):
        long_term = "Long-Term Rental"
        short_term = "Short-Term Rental"
        managed_closed = "Managed - Not For Rent"
        managed_ownership_occupancy = "Managed - Ownership Occupancy"
        no_management = "Not Managed"
        
    class UtilisationStatusChoices(models.TextChoices):
        rented = "Rented"
        vacant = "Vacant"
        remove = "Remove From Market"


    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #last_modified_by = #from users
    property_id = models.PositiveIntegerField(null=False, unique=True)
    buying_contract_date = models.DateField(null=False) #by date
    selling_contract_date = models.DateField(null=False) #by date
    works_needed = models.BooleanField(default=False, null=False)
    #technician = #from sub-contructors
    works_progress = models.CharField(max_length=50, choices=ProgressChoices.choices, default=ProgressChoices.completed, null=False)
    works_notes = models.TextField(blank=True, null=False)
    furniture_needed = models.CharField(max_length=50, choices=FurnitureChoices.choices, default=FurnitureChoices.full, null=False)
    #funiture_provider = #from furniture-providers
    furniture_progress = models.CharField(max_length=50, choices=ProgressChoices.choices, default=ProgressChoices.not_started_yet, null=False)
    furniture_notes = models.TextField(blank=True, null=False)
    utilisation = models.CharField(max_length=50, choices=UtilisationChoices.choices, null=False) #former "status" in PG
    utilisation_status = models.CharField(max_length=50, choices=UtilisationStatusChoices.choices, null=False) #former "status" in PG
    address = models.CharField(max_length=100, null=False)
    municipality = models.CharField(max_length=50, null=False)
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)], null=False)
    floor = models.SmallIntegerField(null=False)
    apartment_no = models.CharField(max_length=10, null=False)
    #owner = #from landlords
    under_rg = models.BooleanField(default=True, null=False)
    rg_ammount = models.DecimalField(max_digits=20, decimal_places=2, null=False)
    rg_percentage = models.PositiveIntegerField(validators=[MaxValueValidator(100)], null=False)
    rg_starting = models.DateField(null=False)
    rg_ending = models.DateField(null=False)
    management_fee = models.DecimalField(max_digits=20, decimal_places=2, null=False)
    actual_rent = models.DecimalField(max_digits=20, decimal_places=2, null=False)
    #tenant = #from tenants
    #rent duration & renewal

class ProperyUtility(models.Model):

    water_registry_no = models.CharField(max_length=20, null=False, blank=True)
    water_meter = models.CharField(max_length=20, null=False, blank=True)
    water_username = models.CharField(max_length=50, null=False, blank=True)
    water_password = models.CharField(max_length=50, null=False, blank=True)
    electricity_provider = models.CharField(max_length=50, null=False, blank=True)
    electricity_utility_no = models.CharField(max_length=20, null=False, blank=True)
    electricity_meter = models.CharField(max_length=20, null=False, blank=True)
    electricity_username = models.CharField(max_length=50, null=False, blank=True)
    electricity_password = models.CharField(max_length=50, null=False, blank=True)
    lng_provider = models.CharField(max_length=50, null=False, blank=True)
    lng_utility_no = models.CharField(max_length=50, null=False, blank=True)
    lng_meter = models.CharField(max_length=50, null=False, blank=True)
    lng_username = models.CharField(max_length=50, null=False, blank=True)
    lng_password = models.CharField(max_length=50, null=False, blank=True)

class PropertyManager(models.Model):

    manager_name = models.CharField(max_length=50, null=False, blank=True)
    manager_phone = models.CharField(max_length=25, null=False, blank=True)
    manager_email = models.EmailField(max_length=50, null=False, blank=True)
    manager_bank_name = models.CharField(max_length=25, null=False, blank=True)
    manager_iban = models.CharField(max_length=25, null=False, blank=True)
    manager_notes = models.TextField(blank=True, null=False)