from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class Legal(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    company_name = models.CharField(max_length=50, null=False) 
    company_address = models.CharField(max_length=50, null=False, blank=True)
    company_municipality = models.CharField(max_length=50, null=False, blank=True)
    company_zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)], null=True, blank=True)
    company_phone = models.CharField(max_length=50, null=False, blank=True)

    class Meta:
        verbose_name_plural = "Legal"

    def __str__(self):
        return f"{self.company_name}"
    
class Electricity(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    company_name = models.CharField(max_length=50, null=False) 
    company_address = models.CharField(max_length=50, null=False, blank=True)
    company_municipality = models.CharField(max_length=50, null=False, blank=True)
    company_zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)], null=True, blank=True)
    company_phone = models.CharField(max_length=50, null=False, blank=True)

    class Meta:
        verbose_name_plural = "Electricity"

    def __str__(self):
        return f"{self.company_name}"
    
class NaturalGas(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    company_name = models.CharField(max_length=50, null=False) 
    company_address = models.CharField(max_length=50, null=False, blank=True)
    company_municipality = models.CharField(max_length=50, null=False, blank=True)
    company_zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)], null=True, blank=True)
    company_phone = models.CharField(max_length=50, null=False, blank=True)

    class Meta:
        verbose_name_plural = "Natural Gas"

    def __str__(self):
        return f"{self.company_name}"


class SubContractor(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    company_name = models.CharField(max_length=50, null=False) 
    company_address = models.CharField(max_length=50, null=False, blank=True)
    company_municipality = models.CharField(max_length=50, null=False, blank=True)
    company_zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)], null=True, blank=True)
    company_phone = models.CharField(max_length=50, null=False, blank=True)

    class Meta:
        verbose_name_plural = "Subcontractors"

    def __str__(self):
        return f"{self.company_name}"

class FurnitureProvider(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    company_name = models.CharField(max_length=50, null=False) 
    company_address = models.CharField(max_length=50, null=False, blank=True)
    company_municipality = models.CharField(max_length=50, null=False, blank=True)
    company_zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)], null=True, blank=True)
    company_phone = models.CharField(max_length=50, null=False, blank=True)

    class Meta:
        verbose_name_plural = "Furniture Providers"

    def __str__(self):
        return f"{self.company_name}"