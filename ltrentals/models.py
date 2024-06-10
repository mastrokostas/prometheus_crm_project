from django.db import models

# Create your models here.

class RenalAgreement(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #rental_agreement_name = #local
    #active = # boolean hidden?

    ## Rental Agreement Details
    #property = # Foreign Key
    #tenant = # Foreign key
    #tenant_2 = # Foreign key
    #actual_rent = # local
    #rental_agreement_starting_date = # local
    #rental_agreement_ending_date = # local
    #rental_agreement_notes = # local
