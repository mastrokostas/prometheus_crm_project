from django import forms

from .models import Property
from landlords.models import Landlord

class AddPropertyForm(forms.ModelForm):

    owner_1 = forms.ModelChoiceField(required=True, queryset=Landlord.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), label="Owner, *Required Choice")
    owner_2 = forms.ModelChoiceField(required=False, queryset=Landlord.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), label="2nd Owner, only if applicable")
    property_id = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Property ID - DO NOT MAKE MISTAKE HERE", "class":"form-control"}), label="*Required")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control",}), label="*Required")
    municipality = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Municipality", "class":"form-control",}), label="*Required")
    zip_code = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Zip Code", "class":"form-control"}), label="*Required")
    floor = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Floor", "class":"form-control"}), label="*Required")
    apartment_no = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Apartment Number", "class":"form-control",}), label="*Required")
    surface = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Surface in sqm (include decimal places if applicable)", "class":"form-control"}), label="*Required")
    buying_contract_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Buying Contract Date, *Required Choise:")
    selling_contract_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Selling Contract Date, *Required Choise:")
    #technician = #from sub-contructors
    works_progress = forms.ChoiceField(required=True, choices=Property.ProgressChoices, widget=forms.Select(attrs={"class":"form-control"}), label="Works Progress, *Required Choise:")
    works_notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"Works Notes", "class":"form-control"}), label="")
    furniture_needed = forms.ChoiceField(required=True, choices=Property.FurnitureChoices, widget=forms.Select(attrs={"class":"form-control"}), label="Furnishing Needed, *Required Choise:")
    #funiture_provider = #from furniture-providers
    furniture_progress = forms.ChoiceField(required=True, choices=Property.ProgressChoices, widget=forms.Select(attrs={"class":"form-control"}), label="Furnishing Progress, *Required Choise:")
    furniture_notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"Furnishing Notes", "class":"form-control"}), label="")
    utilisation = forms.ChoiceField(required=True, choices=Property.UtilisationChoices, widget=forms.Select(attrs={"class":"form-control"}), label="Utilisation, *Required Choise:")
    utilisation_status = forms.ChoiceField(required=False, choices=Property.UtilisationStatusChoices, widget=forms.Select(attrs={"class":"form-control"}), label="Utilisation status, only if applicable:")
    under_rental_guarantee = forms.BooleanField(required=False, label="Rental Guarantee Active")
    rg_ammount = forms.DecimalField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Rental Guarantee Ammount €: (include decimal places if applicable)", "class":"form-control"}), label="")
    rg_percentage = forms.IntegerField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Rental Guarantee Percentage %", "class":"form-control"}), label="")
    rg_starting = forms.DateField(required=False, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Rental Guarantee Starting Date:")
    rg_ending = forms.DateField(required=False, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Rental Guarantee Ending Date:")
    management_fee = forms.DecimalField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Management Fee €: (include decimal places if applicable)", "class":"form-control"}), label="")
    # #actual_rent = models.DecimalField(max_digits=20, decimal_places=2, null=False)
    # #tenant = #from tenants
    # #rent duration & renewal

    class Meta:
        model = Property
        exclude = [
            "created_at", "updated",
        ]


class EditPropertyForm(forms.ModelForm):
    owner_1 = forms.ModelChoiceField(required=True, queryset=Landlord.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), label="Owner, *Required Choice")
    owner_2 = forms.ModelChoiceField(required=False, queryset=Landlord.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), label="2nd Owner, only if applicable")
    property_id = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Property ID - DO NOT MAKE MISTAKE HERE", "class":"form-control"}), label="*Required")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control",}), label="*Required")
    municipality = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Municipality", "class":"form-control",}), label="*Required")
    zip_code = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Zip Code", "class":"form-control"}), label="*Required")
    floor = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Floor", "class":"form-control"}), label="*Required")
    apartment_no = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Apartment Number", "class":"form-control",}), label="*Required")
    surface = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Surface in sqm (include decimal places if applicable)", "class":"form-control"}), label="*Required")
    buying_contract_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Buying Contract Date, *Required Choise:")
    selling_contract_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Selling Contract Date, *Required Choise:")
    #technician = #from sub-contructors
    works_progress = forms.ChoiceField(required=True, choices=Property.ProgressChoices, widget=forms.Select(attrs={"class":"form-control"}), label="Works Progress, *Required Choise:")
    works_notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"Works Notes", "class":"form-control"}), label="")
    furniture_needed = forms.ChoiceField(required=True, choices=Property.FurnitureChoices, widget=forms.Select(attrs={"class":"form-control"}), label="Furnishing Needed, *Required Choise:")
    #funiture_provider = #from furniture-providers
    furniture_progress = forms.ChoiceField(required=True, choices=Property.ProgressChoices, widget=forms.Select(attrs={"class":"form-control"}), label="Furnishing Progress, *Required Choise:")
    furniture_notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"Furnishing Notes", "class":"form-control"}), label="")
    utilisation = forms.ChoiceField(required=True, choices=Property.UtilisationChoices, widget=forms.Select(attrs={"class":"form-control"}), label="Utilisation, *Required Choise:")
    utilisation_status = forms.ChoiceField(required=False, choices=Property.UtilisationStatusChoices, widget=forms.Select(attrs={"class":"form-control"}), label="Utilisation status, only if applicable:")
    under_rental_guarantee = forms.BooleanField(required=False, label="Rental Guarantee Active")
    rg_ammount = forms.DecimalField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Rental Guarantee Ammount €: (include decimal places if applicable)", "class":"form-control"}), label="")
    rg_percentage = forms.IntegerField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Rental Guarantee Percentage %", "class":"form-control"}), label="")
    rg_starting = forms.DateField(required=False, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Rental Guarantee Starting Date:")
    rg_ending = forms.DateField(required=False, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Rental Guarantee Ending Date:")
    management_fee = forms.DecimalField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Management Fee €: (include decimal places if applicable)", "class":"form-control"}), label="")
    # #actual_rent = models.DecimalField(max_digits=20, decimal_places=2, null=False)
    # #tenant = #from tenants
    # #rent duration & renewal 

    class Meta:
        model = Property
        exclude = [
            "created_at", "updated",
        ]