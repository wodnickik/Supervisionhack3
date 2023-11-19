from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(1)]


OFFER_TYPES = [
    ("Lokata", "Lokata"),
    ("Konto oszczędnościowe", "Konto oszczędnościowe")
]


CLIENT_TYPES = [
    ("Indywidualny", "Indywidualny"),
    ("Biznesowy", "Biznesowy")

]

OFFER_KINDS = [
    ("Nowi klienci", "Nowi klienci"),
    ("Starzy klienci", "Starzy klienci"),
    ("Nowe środki", "Nowe środki")
]

CURRENCIES = [
    ("PLN", "PLN"),
    ("EUR", "EUR"),
    ("GBP", "GBP"),
    ("USD", "USD"),
]


class BankOffer(models.Model):
    bank_name = models.TextField(max_length=200, null=False)
    offer_name = models.TextField(max_length=200, null=False)
    interest = models.FloatField(validators=PERCENTAGE_VALIDATOR, null=False)
    offer_type = models.CharField(choices=OFFER_TYPES)
    offer_length_months = models.PositiveIntegerField(null=True)
    client_type = models.CharField(choices=CLIENT_TYPES)
    offer_kind = models.CharField(choices=OFFER_KINDS, null=True)
    min_resources = models.IntegerField(null=True)
    max_resources = models.IntegerField(null=True)
    currency = models.CharField(choices=CURRENCIES)
    additional_info = models.TextField(null=True)
    valid_from_date = models.DateField(null=True)
    dangerous_indicator = models.BooleanField(default=False)




