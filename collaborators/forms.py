from django import forms


from .models import Legal, Electricity, NaturalGas

class EditLegalForm(forms.ModelForm):
    company_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Name", "class":"form-control"}), label="Company Name:")
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
    company_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Name", "class":"form-control"}), label="Company Name:")
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
    company_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Name", "class":"form-control"}), label="Company Name:")
    company_address = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Address", "class":"form-control"}), label="Company Address:")
    company_municipality = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Municipality", "class":"form-control"}), label="Company Municipality:")
    company_zip_code = forms.IntegerField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Zip Code", "class":"form-control"}), label="Zip Code:")
    company_phone = forms.CharField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"Company Phone Number", "class":"form-control"}), label="Company Phone Number:")

    class Meta:
        model = NaturalGas
        exclude = [
            "created_at", "updated",
        ]