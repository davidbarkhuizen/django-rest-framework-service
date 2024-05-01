from django.db import models
from django.core.validators import MinValueValidator

class Currency(models.Model):

    scale = models.IntegerField(validators=[MinValueValidator(0)])
    alpha3 = models.CharField(length = 3, null=False, blank=False)
    numeric3 = models.CharField(length = 3, null=False)
    name = models.CharField(max_length = 100, null=False, blank=False)

    def __str__(self):
        return self.alpha3

class Country(models.Model):

    alpha2 = models.CharField(length = 2, null=False, blank=False)
    alpha3 = models.CharField(length = 3, null=False, blank=False)
    name = models.CharField(max_length = 100, null=False, blank=False)

    currencies = models.ManyToManyField(Currency, through='CountryCurrencies')

    def __str__(self):
        return f'{self.alpha2}: {self.name}'

class CountryCurrencies(models.Model):
    currency = models.ForeignKey(Country)
    country = models.ForeignKey(Currency)