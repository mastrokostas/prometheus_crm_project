from django.db import models
from django.core.validators import MaxValueValidator

from landlords.models import Landlord
from collaborators.models import Electricity, NaturalGas, SubContractor, FurnitureProvider
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
        undecided = "Not Decided Yet"
        long_term = "Long-Term Rental"
        short_term = "Short-Term Rental"
        managed_closed = "Managed - Not For Rent"
        managed_ownership_occupancy = "Managed - Ownership Occupancy"
        no_management = "Not Managed"
        
    class UtilisationStatusChoices(models.TextChoices):
        none = "None"
        rented = "Rented"
        vacant = "Vacant"
        remove_from_market = "Remove From Market"

    ## Auto Fill
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    ## Owner
    owner_1 = models.ForeignKey(Landlord, null=True, on_delete=models.PROTECT, related_name="property_owner_1")
    owner_2 = models.ForeignKey(Landlord, null=True, blank=True, on_delete=models.PROTECT, related_name="property_owner_2")

    ## Property Stuff
    property_id = models.PositiveIntegerField(null=False, unique=True)
    address = models.CharField(max_length=100, null=False)
    municipality = models.CharField(max_length=50, null=False)
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)], null=False)
    floor = models.SmallIntegerField(null=False)
    apartment_no = models.CharField(max_length=10, null=False)
    surface = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    buying_contract_date = models.DateField(null=False) #by date
    selling_contract_date = models.DateField(null=False) #by date

    ## Construction
    sub_contractor = models.ForeignKey(SubContractor, null=True, on_delete=models.PROTECT, related_name="sub_contractor")
    works_progress = models.CharField(max_length=50, choices=ProgressChoices.choices, default=ProgressChoices.completed, null=False)
    works_notes = models.TextField(blank=True, null=False)

    # Furnishing
    furniture_needed = models.CharField(max_length=50, choices=FurnitureChoices.choices, default=FurnitureChoices.full, null=False)
    funiture_provider = models.ForeignKey(FurnitureProvider, null=True, on_delete=models.PROTECT, related_name="furniture_provider")
    furniture_progress = models.CharField(max_length=50, choices=ProgressChoices.choices, default=ProgressChoices.not_started_yet, null=False)
    furniture_notes = models.TextField(blank=True, null=False)

    ## Utilisation
    utilisation = models.CharField(max_length=50, choices=UtilisationChoices.choices, null=False) #former "status" in PG
    utilisation_status = models.CharField(max_length=50, choices=UtilisationStatusChoices.choices, null=False, blank=True) #former "status" in PG

    ## Rental Guarantee
    under_rental_guarantee = models.BooleanField(default=False, null=True)
    rg_ammount = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    rg_percentage = models.PositiveIntegerField(validators=[MaxValueValidator(100)], null=True)
    rg_starting = models.DateField(null=True)
    rg_ending = models.DateField(null=True)

    management_fee = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    #actual_rent = models.DecimalField(max_digits=20, decimal_places=2, null=False)
    #tenant = #from tenants
    #rent duration & renewal

    ## Utilities
    water_registry_no = models.CharField(max_length=20, null=False, blank=True)
    water_meter = models.CharField(max_length=20, null=False, blank=True)
    water_username = models.CharField(max_length=50, null=False, blank=True)
    water_password = models.CharField(max_length=50, null=False, blank=True)
    electricity_provider = models.ForeignKey(Electricity, null=True, on_delete=models.PROTECT, related_name="electricity")
    electricity_utility_no = models.CharField(max_length=20, null=False, blank=True)
    electricity_meter = models.CharField(max_length=20, null=False, blank=True)
    electricity_username = models.CharField(max_length=50, null=False, blank=True)
    electricity_password = models.CharField(max_length=50, null=False, blank=True)
    lng_provider = models.ForeignKey(NaturalGas, null=True, on_delete=models.PROTECT, related_name="natural_gas")
    lng_utility_no = models.CharField(max_length=50, null=False, blank=True)
    lng_meter = models.CharField(max_length=50, null=False, blank=True)
    lng_username = models.CharField(max_length=50, null=False, blank=True)
    lng_password = models.CharField(max_length=50, null=False, blank=True)

    class Meta:
        verbose_name_plural = "Properties"

    def __str__(self):
        return f"{self.address} {self.municipality}"
    

class PropertyBuildingManager(models.Model):

    manager_name = models.CharField(max_length=50, null=False, blank=True)
    manager_phone = models.CharField(max_length=25, null=False, blank=True)
    manager_email = models.EmailField(max_length=50, null=False, blank=True)
    manager_bank_name = models.CharField(max_length=25, null=False, blank=True)
    manager_iban = models.CharField(max_length=25, null=False, blank=True)
    manager_notes = models.TextField(blank=True, null=False)