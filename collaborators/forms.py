from django import forms


from .models import Legal, Electricity, NaturalGas, BuildingManagementCompany, SubContractor

class EditLegalForm(forms.ModelForm):
    company_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Name", "class":"form-control"}), label="Company Name, *Required:")
    company_address = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Address", "class":"form-control"}), label="Company Address:")
    company_municipality = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Municipality", "class":"form-control"}), label="Company Municipality:")
    company_zip_code = forms.IntegerField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Zip Code", "class":"form-control"}), label="Zip Code:")
    company_phone = forms.CharField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Company Phone Number", "class":"form-control"}), label="Company Phone Number:")

    class Meta:
        model = Legal
        exclude = [
            "created_at", "updated",
        ]

class EditElectricityForm(forms.ModelForm):
    company_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Name", "class":"form-control"}), label="Company Name, *Required:")
    company_address = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Address", "class":"form-control"}), label="Company Address:")
    company_municipality = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Municipality", "class":"form-control"}), label="Company Municipality:")
    company_zip_code = forms.IntegerField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Zip Code", "class":"form-control"}), label="Zip Code:")
    company_phone = forms.CharField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Company Phone Number", "class":"form-control"}), label="Company Phone Number:")

    class Meta:
        model = Electricity
        exclude = [
            "created_at", "updated",
        ]

class EditNaturalGasForm(forms.ModelForm):
    company_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Name", "class":"form-control"}), label="Company Name, *Required:")
    company_address = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Address", "class":"form-control"}), label="Company Address:")
    company_municipality = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Municipality", "class":"form-control"}), label="Company Municipality:")
    company_zip_code = forms.IntegerField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Zip Code", "class":"form-control"}), label="Zip Code:")
    company_phone = forms.CharField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Company Phone Number", "class":"form-control"}), label="Company Phone Number:")

    class Meta:
        model = NaturalGas
        exclude = [
            "created_at", "updated",
        ]

class EditBuildingManagerForm(forms.ModelForm):
    company_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Name", "class":"form-control"}), label="Company Name, *Required:")
    company_address = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Address", "class":"form-control"}), label="Company Address:")
    company_municipality = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Municipality", "class":"form-control"}), label="Company Municipality:")
    company_zip_code = forms.IntegerField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Zip Code", "class":"form-control"}), label="Zip Code:")
    company_phone = forms.CharField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Company Phone Number", "class":"form-control"}), label="Company Phone Number:")
    designated_person_first_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Designated Person First Name", "class":"form-control"}), label="Designated Person First Name:")
    designated_person_last_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Designated Person First Name", "class":"form-control"}), label="Designated Person First Name:")

    class Meta:
        model = BuildingManagementCompany
        exclude = [
            "created_at", "updated",
        ]

class EditSubContractorForm(forms.ModelForm):
    company_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Name", "class":"form-control"}), label="Company Name, *Required:")
    company_address = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Address", "class":"form-control"}), label="Company Address:")
    company_municipality = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Municipality", "class":"form-control"}), label="Company Municipality:")
    company_zip_code = forms.IntegerField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Zip Code", "class":"form-control"}), label="Zip Code:")
    company_phone = forms.CharField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Company Phone Number", "class":"form-control"}), label="Company Phone Number:")

    class Meta:
        model = SubContractor
        exclude = [
            "created_at", "updated",
        ]