from django import forms

from .models import RentalAgreement
from properties.models import Property
from tenants.models import Tenant

class AddRentalAgreementForm(forms.ModelForm):

    rental_agreement_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Rental Agreement Name", "class":"form-control"}), label="Rental Agreement Name, *Required:")
    property = forms.ModelChoiceField(required=True, queryset=Property.objects.filter(utilisation="Long-Term Rental").filter(utilisation_status="Vacant"), widget=forms.Select(attrs={"class":"form-control"}), label="Select Property, *Required:")
    tenant = forms.ModelChoiceField(required=True, queryset=Tenant.objects.filter(is_blacklisted=False).order_by('last_name'), widget=forms.Select(attrs={"class":"form-control"}), label="Select Tenant, *Required:")
    tenant_2 = forms.ModelChoiceField(required=False, queryset=Tenant.objects.filter(is_blacklisted=False).order_by('last_name'), widget=forms.Select(attrs={"class":"form-control"}), label="Select Second Tenant If Applicable:")
    actual_rent = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Rent €: (include decimal places if applicable)", "class":"form-control"}), label="Rent, *Required:")
    security_deposits = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"class":"form-control"}), label="Security Deposits Paid, *Required:")
    rental_agreement_starting_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Select Rental Agreement Starting Date, *Required:")
    rental_agreement_ending_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Select Rental Agreement Ending Date, *Required:")
    rental_agreement_notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"Rental Agreement Notes", "class":"form-control"}), label="Rental Agreement Notes:")

    class Meta:
        model = RentalAgreement
        exclude = [
            "created_at", "updated", "is_active",
        ]

class EditRentalAgreementForm(forms.ModelForm):

    rental_agreement_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Rental Agreement Name", "class":"form-control"}), label="Rental Agreement Name, *Required:")
    tenant = forms.ModelChoiceField(required=True, queryset=Tenant.objects.filter(is_blacklisted=False).order_by('last_name'), widget=forms.Select(attrs={"class":"form-control"}), label="Select Tenant, *Required:")
    tenant_2 = forms.ModelChoiceField(required=False, queryset=Tenant.objects.filter(is_blacklisted=False).order_by('last_name'), widget=forms.Select(attrs={"class":"form-control"}), label="Select Second Tenant If Applicable:")
    actual_rent = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Rent €: (include decimal places if applicable)", "class":"form-control"}), label="Rent, *Required:")
    security_deposits = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"class":"form-control"}), label="Security Deposits Paid, *Required:")
    rental_agreement_starting_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Select Rental Agreement Starting Date, *Required:")
    rental_agreement_ending_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Select Rental Agreement Ending Date, *Required:")
    rental_agreement_notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"Rental Agreement Notes", "class":"form-control"}), label="Rental Agreement Notes:")

    class Meta:
        model = RentalAgreement
        exclude = [
            "created_at", "updated", "is_active", "property"
        ]

class TerminateRentalAgreementForm(forms.ModelForm):
    rental_agreement_ending_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Select Rental Agreement Ending Date, *Required:")
    rental_agreement_notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"Rental Agreement Notes", "class":"form-control"}), label="Rental Agreement Notes:")

    class Meta:
        model = RentalAgreement
        exclude = [
            "created_at", "updated", "is_active", "rental_agreement_name", "property", "tenant", "tenant_2", "actual_rent", "security_deposits", "rental_agreement_starting_date",
        ]