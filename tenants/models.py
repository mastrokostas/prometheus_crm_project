from django.db import models

# Create your models here.

class Tenant(models.Model):

    ID_CHOICES = {
        "id_card" : "Id Card",
        "passport" : "Passport",
    }

    NATIONALITY_CHOICES = {
        "GR" : "GR",
        "UK" : "UK",
    }


    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    fathers_name = models.CharField(max_length=100, blank=True, null=False)
    phone = models.IntegerField(blank=True, null=True)
    phone_2 = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank= True, null=False)
    tax_id = models.PositiveIntegerField(null=False, unique=True)
    tax_office = models.CharField(max_length=100, blank=True, null=False)
    id_type = models.CharField(max_length=30, choices=ID_CHOICES, null=False)
    id_number = models.CharField(max_length=50, null=False)
    nationality = models.CharField(max_length=50, choices=NATIONALITY_CHOICES, null=False)
    is_active = models.BooleanField(default=False, null=False)
    is_blacklisted = models.BooleanField(default=False, null=False)
    legal_action = models.BooleanField(default=False, null=False)
    notes = models.TextField(blank=True, null=False)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"