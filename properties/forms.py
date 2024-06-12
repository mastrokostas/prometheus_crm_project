from django import forms

from .models import Property
from landlords.models import Landlord
from collaborators.models import SubContractor, FurnitureProvider, Electricity, NaturalGas, BuildingManagementCompany

class AddPropertyForm(forms.ModelForm):

    ## Owner
    owner_1 = forms.ModelChoiceField(required=True, queryset=Landlord.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), label="Owner, *Required Choice:")
    owner_2 = forms.ModelChoiceField(required=False, queryset=Landlord.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), label="2nd Owner, only if applicable:")

    ## Property Stuff
    property_id = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Property ID - DO NOT MAKE MISTAKE HERE", "class":"form-control"}), label="Property ID, *Required:")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control",}), label="Address, *Required:")
    municipality = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Municipality", "class":"form-control",}), label="Municipality, *Required:")
    zip_code = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Zip Code", "class":"form-control"}), label="Zip Code, *Required:")
    floor = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Floor", "class":"form-control"}), label="Floor, *Required:")
    apartment_no = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Apartment Number", "class":"form-control",}), label="Apartment Number, *Required:")
    surface = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Surface in sqm (include decimal places if applicable)", "class":"form-control"}), label="Surface, *Required:")
    buying_contract_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Buying Contract Date, *Required Choise:")
    selling_contract_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Selling Contract Date, *Required Choise:")

    ## Construction
    constructed_by = forms.ChoiceField(required=True, choices=Property.ConstructedByChoises, widget=forms.Select(attrs={"class":"form-control"}), label="Constructed By, *Required Choise:")
    sub_contractor = forms.ModelChoiceField(required=True, queryset=SubContractor.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), label="Sub-Contractor:")
    works_progress = forms.ChoiceField(required=True, choices=Property.ProgressChoices, widget=forms.Select(attrs={"class":"form-control"}), label="Works Progress, *Required Choise:")
    works_notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"Works Notes", "class":"form-control"}), label="Works Notes:")

    ## Furnishing
    furniture_needed = forms.ChoiceField(required=True, choices=Property.FurnitureChoices, widget=forms.Select(attrs={"class":"form-control"}), label="Furnishing Needed, *Required Choise:")
    furniture_provider = forms.ModelChoiceField(required=True, queryset=FurnitureProvider.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), label="Furniture Provider, *Required Choise:")
    furniture_progress = forms.ChoiceField(required=True, choices=Property.ProgressChoices, widget=forms.Select(attrs={"class":"form-control"}), label="Furnishing Progress, *Required Choise:")
    furniture_notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"Furnishing Notes", "class":"form-control"}), label="Furnishing Notes:")

    ## Utilisation
    utilisation = forms.ChoiceField(required=True, choices=Property.UtilisationChoices, widget=forms.Select(attrs={"class":"form-control"}), label="Utilisation, *Required Choise:")
    #utilisation_status = forms.ChoiceField(required=False, choices=Property.UtilisationStatusChoices, widget=forms.Select(attrs={"class":"form-control"}), label="Utilisation status, only if applicable:")

    ## Rental Guarantee
    under_rental_guarantee = forms.BooleanField(required=False, label="Rental Guarantee Active?")
    rg_ammount = forms.DecimalField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Rental Guarantee Ammount €: (include decimal places if applicable)", "class":"form-control"}), label="Rental Guarantee Ammount:")
    rg_percentage = forms.IntegerField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Rental Guarantee Percentage %", "class":"form-control"}), label="Rental Guarantee Percentage:")
    rg_starting = forms.DateField(required=False, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Rental Guarantee Starting Date:")
    rg_ending = forms.DateField(required=False, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Rental Guarantee Ending Date:")
    

    ## Management
    management_fee = forms.DecimalField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Management Fee €: (include decimal places if applicable)", "class":"form-control"}), label="Management Fee:")
    building_management_company = forms.ModelChoiceField(required=True, queryset=BuildingManagementCompany.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), label="Building Management Company, *Required:")
    building_manager_first_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Building Manager First Name", "class":"form-control"}), label="Building Manager First Name:")
    building_manager_last_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Building Manager Last Name", "class":"form-control"}), label="Building Manager Last Name:")
    building_manager_phone = forms.IntegerField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Building Manager Phone Number", "class":"form-control"}), label="Building Manager Phone Number:")
    building_manager_apt = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Building Manager Apartment Number", "class":"form-control",}), label="Building Manager Apartment Number:")

    ## Utilities
    water_registry_no = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Water Registry Number", "class":"form-control",}), label="Water Registry Number:")
    water_meter = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Water Meter", "class":"form-control",}), label="Water Meter:")
    water_username = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"EDYAP Username", "class":"form-control",}), label="EDYAP Username:")
    water_password = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"EYDAP Password", "class":"form-control",}), label="EDYAP Password:")
    electricity_provider = forms.ModelChoiceField(required=True, queryset=Electricity.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), label="Electricity Provider, *Required:")
    electricity_utility_no = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Electricity Utility Number", "class":"form-control",}), label="Electricity Utility Number:")
    electricity_meter = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Electricity Meter", "class":"form-control",}), label="Electricity Meter:")
    electricity_username = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Electricity Provider Username", "class":"form-control",}), label="Electricity Provider Username:")
    electricity_password = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Electricity Provider Password", "class":"form-control",}), label="Electricity Provider Password:")
    lng_provider = forms.ModelChoiceField(required=True, queryset=NaturalGas.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), label="Natural Gas Provider, *Required:")
    lng_utility_no = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Natural Gas Utility Number", "class":"form-control",}), label="Natural Gas Utility Number:")
    lng_meter = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Natural Gas Meter", "class":"form-control",}), label="Natural Gas Meter:")
    lng_username = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Natural Gas Provider Username", "class":"form-control",}), label="Natural Gas Provider Username:")
    lng_password = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Natural Gas Provider Password", "class":"form-control",}), label="Natural Gas Provider Password:")

    class Meta:
        model = Property
        exclude = [
            "created_at", "updated", "utilisation_status", "rg_expiring",
        ]


class EditPropertyForm(forms.ModelForm):

    ## Owner
    owner_1 = forms.ModelChoiceField(required=True, queryset=Landlord.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), label="Owner, *Required Choice:")
    owner_2 = forms.ModelChoiceField(required=False, queryset=Landlord.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), label="2nd Owner, only if applicable:")

    ## Property Stuff
    property_id = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Property ID - DO NOT MAKE MISTAKE HERE", "class":"form-control"}), label="Property ID, *Required:")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control",}), label="*Required")
    municipality = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Municipality", "class":"form-control",}), label="Address, *Required:")
    zip_code = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Zip Code", "class":"form-control"}), label="Municipality, *Required:")
    floor = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Floor", "class":"form-control"}), label="Zip Code, *Required:")
    apartment_no = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Apartment Number", "class":"form-control",}), label="Apartment Number, *Required:")
    surface = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Surface in sqm (include decimal places if applicable)", "class":"form-control"}), label="Surface, *Required:")
    buying_contract_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Buying Contract Date, *Required Choise:")
    selling_contract_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Selling Contract Date, *Required Choise:")

    ## Construction
    constructed_by = forms.ChoiceField(required=True, choices=Property.ConstructedByChoises, widget=forms.Select(attrs={"class":"form-control"}), label="Constructed By, *Required Choise:")
    sub_contractor = forms.ModelChoiceField(required=True, queryset=SubContractor.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), label="Sub-Contractor:")
    works_progress = forms.ChoiceField(required=True, choices=Property.ProgressChoices, widget=forms.Select(attrs={"class":"form-control"}), label="Works Progress, *Required Choise:")
    works_notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"Works Notes", "class":"form-control"}), label="Works Notes:")

    ## Furnishing
    furniture_needed = forms.ChoiceField(required=True, choices=Property.FurnitureChoices, widget=forms.Select(attrs={"class":"form-control"}), label="Furnishing Needed, *Required Choise:")
    furniture_provider = forms.ModelChoiceField(required=True, queryset=FurnitureProvider.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), label="Furniture Provider, *Required Choise:")
    furniture_progress = forms.ChoiceField(required=True, choices=Property.ProgressChoices, widget=forms.Select(attrs={"class":"form-control"}), label="Furnishing Progress, *Required Choise:")
    furniture_notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"Furnishing Notes", "class":"form-control"}), label="Furnishing Notes:")

    ## Utilisation
    utilisation = forms.ChoiceField(required=True, choices=Property.UtilisationChoices, widget=forms.Select(attrs={"class":"form-control"}), label="Utilisation, *Required Choise:")
    #utilisation_status = forms.ChoiceField(required=False, choices=Property.UtilisationStatusChoices, widget=forms.Select(attrs={"class":"form-control"}), label="Utilisation status, only if applicable:")

    ## Rental Guarantee
    under_rental_guarantee = forms.BooleanField(required=False, label="Rental Guarantee Active?")
    rg_ammount = forms.DecimalField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Rental Guarantee Ammount €: (include decimal places if applicable)", "class":"form-control"}), label="Rental Guarantee Ammount:")
    rg_percentage = forms.IntegerField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Rental Guarantee Percentage %", "class":"form-control"}), label="Rental Guarantee Percentage:")
    rg_starting = forms.DateField(required=False, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Rental Guarantee Starting Date:")
    rg_ending = forms.DateField(required=False, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Rental Guarantee Ending Date:")
    
    management_fee = forms.DecimalField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Management Fee €: (include decimal places if applicable)", "class":"form-control"}), label="Management Fee:")
    building_management_company = forms.ModelChoiceField(required=True, queryset=BuildingManagementCompany.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), label="Building Management Company, *Required:")
    building_manager_first_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Building Manager First Name", "class":"form-control"}), label="Building Manager First Name:")
    building_manager_last_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Building Manager Last Name", "class":"form-control"}), label="Building Manager Last Name:")
    building_manager_phone = forms.IntegerField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Building Manager Phone Number", "class":"form-control"}), label="Building Manager Phone Number:")
    building_manager_apt = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Building Manager Apartment Number", "class":"form-control",}), label="Building Manager Apartment Number:")
    # #actual_rent = models.DecimalField(max_digits=20, decimal_places=2, null=False)
    # #tenant = #from tenants
    # #rent duration & renewal

    ## Utilities
    water_registry_no = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Water Registry Number", "class":"form-control",}), label="Water Registry Number:")
    water_meter = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Water Meter", "class":"form-control",}), label="Water Meter:")
    water_username = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"EDYAP Username", "class":"form-control",}), label="EDYAP Username:")
    water_password = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"EYDAP Password", "class":"form-control",}), label="EDYAP Password:")
    electricity_provider = forms.ModelChoiceField(required=True, queryset=Electricity.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), label="Electricity Provider, *Required:")
    electricity_utility_no = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Electricity Utility Number", "class":"form-control",}), label="Electricity Utility Number:")
    electricity_meter = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Electricity Meter", "class":"form-control",}), label="Electricity Meter:")
    electricity_username = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Electricity Provider Username", "class":"form-control",}), label="Electricity Provider Username:")
    electricity_password = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Electricity Provider Password", "class":"form-control",}), label="Electricity Provider Password:")
    lng_provider = forms.ModelChoiceField(required=False, queryset=NaturalGas.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), label="Natural Gas Provider:")
    lng_utility_no = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Natural Gas Utility Number", "class":"form-control",}), label="Natural Gas Utility Number, *Required:")
    lng_meter = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Natural Gas Meter", "class":"form-control",}), label="Natural Gas Meter:")
    lng_username = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Natural Gas Provider Username", "class":"form-control",}), label="Natural Gas Provider Username:")
    lng_password = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Natural Gas Provider Password", "class":"form-control",}), label="Natural Gas Provider Password:")

    class Meta:
        model = Property
        exclude = [
            "created_at", "updated", "rg_expiring", "utilisation_status",
        ]

class EditUtilisationInformationForm(forms.ModelForm):

    UTILISATION_STATUS_CHOICES = {
        "Vacant" : "Vacant",
        "Remove From Market" : "Remove From Market",
    }
    
    utilisation_status = forms.CharField(required=False, widget=forms.Select(attrs={"class":"form-control"}, choices=UTILISATION_STATUS_CHOICES), label="Utilisation status:")


    #forms.CharField(required=True, widget=forms.Select(attrs={"class":"form-control"}, choices=NATIONALITY_CHOICES), label="Nationality, *Required Choice:")

    class Meta:
        model = Property
        fields = [
            "utilisation_status",
        ]