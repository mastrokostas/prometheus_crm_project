from django import forms

from .models import Tenant


ID_CHOICES = {
        "id_card" : "ID Card",
        "passport" : "Passport",
    }

NATIONALITY_CHOICES = {
        "GR" : "Greek",
        "UK" : "British",
    }

class AddTenantForm(forms.ModelForm):
    
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="*Required")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="*Required")
    fathers_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Father's Name", "class":"form-control"}), label="")
    phone = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone Number", "class":"form-control"}), label="")
    phone_2 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone Number 2", "class":"form-control"}), label="")
    email = forms.EmailField(required=False, widget=forms.widgets.EmailInput(attrs={"placeholder":"email@domain.tdl", "class":"form-control"}), label="")
    tax_id = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Tax ID Number", "class":"form-control"}), label="*Required")
    tax_office = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Tax Office", "class":"form-control"}), label="")
    id_type = forms.CharField(required=True, widget=forms.Select(attrs={"class":"form-control"}, choices=ID_CHOICES), label="Identification Type, *Required Choice")
    id_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"ID or Passport Number", "class":"form-control"}), label="*Required")
    nationality = forms.CharField(required=True, widget=forms.Select(attrs={"class":"form-control"}, choices=NATIONALITY_CHOICES), label="Nationality, *Required Choice")

    class Meta:
        model = Tenant
        exclude = [
            "created_at", "updated", "is_active", "is_blacklisted",
        ]


class EditTenantForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    fathers_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Father's Name", "class":"form-control"}), label="")
    phone = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone Number", "class":"form-control"}), label="")
    phone_2 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone Number 2", "class":"form-control"}), label="")
    email = forms.EmailField(required=False, widget=forms.widgets.EmailInput(attrs={"placeholder":"email@domain.tdl", "class":"form-control"}), label="")
    tax_id = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Tax ID Number", "class":"form-control"}), label="")
    tax_office = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Tax Office", "class":"form-control"}), label="")
    id_type = forms.CharField(required=True, widget=forms.Select(attrs={"class":"form-control"}, choices=ID_CHOICES), label="Identification Type:")
    id_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"ID or Passport Number", "class":"form-control"}), label="")
    is_active = forms.BooleanField(required=False)
    is_blacklisted = forms.BooleanField(required=False)

    class Meta:
        model = Tenant
        exclude = [
            "created_at", "updated",
        ]