from django.db import models

# Create your models here.

class Landlord(models.Model):

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

    LAW_FIRM_CHOICES = {
        "K/P" : "K/P",
        "KMD" : "KMD",
    }

    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    file_type = models.CharField(max_length=2, choices=FILE_TYPE_CHOICES, null=False)
    file_number = models.PositiveSmallIntegerField(null=False) #, unique=True will conflict with M
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    fathers_name = models.CharField(max_length=100, blank=True, null=False)
    phone = models.IntegerField(blank=True, null=True)
    phone_2 = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank= True, null=False)
    tax_id = models.PositiveIntegerField(null=False, unique=True)
    tax_office = models.CharField(max_length=100, blank=True, null=False)
    passport_number = models.CharField(max_length=50, null=False)
    passport_expiry_date = models.DateField(null=False)
    nationality = models.CharField(max_length=50, choices=NATIONALITY_CHOICES, null=False)
    law_firm = models.CharField(max_length=50, choices=LAW_FIRM_CHOICES, null=False)
    cooperation_type = models.CharField(max_length=50, choices=COOPERATION_TYPE_CHOICES, null=False)
    is_active = models.BooleanField(default=False, null=False)
    is_blacklisted = models.BooleanField(default=False, null=False)
    notes = models.TextField(blank=True, null=False)

    #accountnat
    #law firm

    def __str__(self):
        return f"F.{self.file_number} {self.last_name} {self.first_name}"