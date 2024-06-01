from django.db import models

# Create your models here.

class Tenant(models.Model):

    class IdDocumentChoices(models.TextChoices):
        id_card = "Id Card"
        passport = "Passport"

    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    fathers_name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, blank=True, null=False)
    email = models.EmailField(blank= True, null=False)
    tax_id = models.PositiveIntegerField(null=False, unique=True)
    tax_office = models.CharField(max_length=100, blank=True, null=False)
    id_type = models.CharField(max_length=30, choices=IdDocumentChoices.choices, null=False)
    id_number = models.CharField(max_length=50, null=False)
    is_active = models.BooleanField(default=True, null=False)
    is_blacklisted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"