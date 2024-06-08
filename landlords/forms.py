from django import forms

from .models import Landlord
from collaborators.models import Legal

NATIONALITY_CHOICES = {
        "CN" : "CN",
        "GR" : "GR",
        "UK" : "UK",
    }

FILE_TYPE_CHOICES = {
    "F" : "F",
    "M" : "M",
}

COOPERATION_TYPE_CHOICES = {
        "FULL" : "FULL",
        "ONLY PR" : "ONLY PR",
        "ONLY MANAGEMENT" : "ONLY MANAGEMENT",
        "NONE" : "NONE",
    }

class AddLandlordForm(forms.ModelForm):
    file_type = forms.CharField(required=True, widget=forms.Select(attrs={"class":"form-control"}, choices=FILE_TYPE_CHOICES), label="File Type, *Required Choice:")
    file_number = forms.IntegerField(required=True, min_value=0, widget=forms.NumberInput(attrs={"placeholder":"File Number", "class":"form-control"}), label="File Number, *Required:")
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="First Name, *Required:")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="Last Name, *Required:")
    fathers_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Father's Name", "class":"form-control"}), label="Father's Name:")
    phone = forms.IntegerField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Phone Number", "class":"form-control"}), label="Phone Number:")
    phone_2 = forms.IntegerField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Phone Number 2", "class":"form-control"}), label="Phone Number 2:")
    email = forms.EmailField(required=False, widget=forms.widgets.EmailInput(attrs={"placeholder":"email@domain.tdl", "class":"form-control"}), label="Email:")
    tax_id = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Tax ID Number", "class":"form-control"}), label="Tax ID Number, *Required:")
    tax_office = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Tax Office", "class":"form-control"}), label="Tax Office:")
    nationality = forms.CharField(required=True, widget=forms.Select(attrs={"class":"form-control"}, choices=NATIONALITY_CHOICES), label="Nationality, *Required Choice:")
    law_firm = forms.ModelChoiceField(required=True, queryset=Legal.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), label="Law Firm, *Required Choice:")
    passport_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"ID or Passport Number", "class":"form-control"}), label="ID or Passport Number, *Required:")
    passport_expiry_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Passport Expiry Date, *Required Choice:")
    cooperation_type = forms.CharField(required=True, widget=forms.Select(attrs={"class":"form-control"}, choices=COOPERATION_TYPE_CHOICES), label="Cooperation Type, *Required Choice:")
    notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"Notes for Landlord", "class":"form-control"}), label="Notes for Landlord:")
    
    class Meta:
        model = Landlord
        exclude = [
            "created_at", "updated", "is_active", "is_blacklisted",
        ]

class EditLandlordForm(forms.ModelForm):
    file_type = forms.CharField(required=True, widget=forms.Select(attrs={"class":"form-control"}, choices=FILE_TYPE_CHOICES), label="File Type, *Required Choice:")
    file_number = forms.IntegerField(required=True, min_value=0, widget=forms.NumberInput(attrs={"placeholder":"File Number", "class":"form-control"}), label="File Number, *Required:")
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="First Name, *Required:")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="Last Name, *Required:")
    fathers_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Father's Name", "class":"form-control"}), label="Father's Name:")
    phone = forms.IntegerField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Phone Number", "class":"form-control"}), label="Phone Number:")
    phone_2 = forms.IntegerField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Phone Number 2", "class":"form-control"}), label="Phone Number 2:")
    email = forms.EmailField(required=False, widget=forms.widgets.EmailInput(attrs={"placeholder":"email@domain.tdl", "class":"form-control"}), label="Email:")
    tax_id = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Tax ID Number", "class":"form-control"}), label="Tax ID Number, *Required:")
    tax_office = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Tax Office", "class":"form-control"}), label="Tax Office:")
    nationality = forms.CharField(required=True, widget=forms.Select(attrs={"class":"form-control"}, choices=NATIONALITY_CHOICES), label="Nationality, *Required Choice:")
    law_firm = forms.ModelChoiceField(required=True, queryset=Legal.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), label="Law Firm, *Required Choice:")
    passport_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"ID or Passport Number", "class":"form-control"}), label="ID or Passport Number, *Required:")
    passport_expiry_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Passport Expiry Date, *Required Choice:")
    cooperation_type = forms.CharField(required=True, widget=forms.Select(attrs={"class":"form-control"}, choices=COOPERATION_TYPE_CHOICES), label="Cooperation Type, *Required Choice:")
    is_active = forms.BooleanField(required=False)
    is_blacklisted = forms.BooleanField(required=False)
    notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"Notes for Landlord", "class":"form-control"}), label="Notes for Landlord:")

    class Meta:
        model = Landlord
        exclude = [
            "created_at", "updated",
        ]