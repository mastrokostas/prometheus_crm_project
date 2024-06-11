from django.db import models

from properties.models import Property
from tenants.models import Tenant

# Create your models here.

class RentalAgreement(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    rental_agreement_name = models.CharField(max_length=100, null=False)
    is_active = models.BooleanField(default=True, null=False)

    ## Rental Agreement Details
    property = models.ForeignKey(Property, null=True, blank=False, on_delete=models.CASCADE, related_name="property")
    tenant = models.ForeignKey(Tenant, null=True, blank=False, on_delete=models.CASCADE, related_name="tenant")
    tenant_2 = models.ForeignKey(Tenant, null=True, blank=True, on_delete=models.CASCADE, related_name="tenant_2")
    actual_rent = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    security_deposits = models.PositiveSmallIntegerField(null=False, default=2)
    rental_agreement_starting_date = models.DateField(null=True, blank=False)
    rental_agreement_ending_date = models.DateField(null=True, blank=False)
    rental_agreement_notes = models.TextField(null=False, blank=True)
    total_months = models.PositiveSmallIntegerField(null=False)
    months_paid = models.PositiveSmallIntegerField(null=False)
    months_remaining = models.PositiveSmallIntegerField(null=False)
    months_owed = models.PositiveSmallIntegerField(null=False)
    #payments = models.ForeignKey(MonthlyPayment, null=True, blank=False, on_delete=models.CASCADE, related_name="payments")

    def __str__(self):
        return f"{self.tenant} {self.rental_agreement_name}"
    

class MonthlyPayment(models.Model):

    class PaymentChoices(models.TextChoices):
        cash = "Cash"
        pir = "PIR"

    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #property = models.ForeignKey(RentalAgreement, null=True, blank=False, on_delete=models.CASCADE, related_name="payment_property")
    rental_agreement = models.ForeignKey(RentalAgreement, null=True, blank=False, on_delete=models.CASCADE, related_name="rental_agreement")
    
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    payment_date = models.DateField(null=True, blank=False)
    payment_mehtod = models.CharField(null=False, max_length=20, choices=PaymentChoices.choices, default=PaymentChoices.pir)
    paid_month = models.DateField(null=True, blank=False)
    #paid_year = models.DateField(null=True, blank=False)
    #months_due = models.PositiveSmallIntegerField(null=False)
