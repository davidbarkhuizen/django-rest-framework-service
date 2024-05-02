from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator

alpha_only = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')
numeric_only = RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')

class Currency(models.Model):

    scale = models.IntegerField(validators=[MinValueValidator(0)])
    alpha3 = models.CharField(max_length=3, validators=[MinLengthValidator(3), alpha_only])
    numeric3 = models.CharField(max_length=3, validators=[MinLengthValidator(3), numeric_only])
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.alpha3

class Country(models.Model):

    alpha2 = models.CharField(max_length=2, validators=[MinLengthValidator(2), alpha_only])
    alpha3 = models.CharField(max_length=3, validators=[MinLengthValidator(3), alpha_only])
    currencies = models.ManyToManyField(Currency, through='CountryCurrencies')
    deleted_date = models.DateTimeField(default=None, null=True)
    name = models.CharField(max_length = 100)
    numeric3 = models.CharField(max_length=3, validators=[MinLengthValidator(3), numeric_only])

    def __str__(self):
        return f'{self.alpha2}: {self.name}'

class CountryCurrencies(models.Model):

    currency = models.ForeignKey(Country, on_delete=models.CASCADE)
    country = models.ForeignKey(Currency, on_delete=models.CASCADE)
