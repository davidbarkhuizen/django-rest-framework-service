from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

alpha_only = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')
numeric_only = RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')

class Country(models.Model):

    alpha2 = models.CharField(max_length=2, validators=[MinLengthValidator(2), alpha_only])
    alpha3 = models.CharField(max_length=3, validators=[MinLengthValidator(3), alpha_only])
    currencies = models.JSONField()
    deleted_date = models.BooleanField(default=None, null=True)
    name = models.CharField(max_length = 100)
    number3 = models.CharField(max_length=3, validators=[MinLengthValidator(3), numeric_only])

    def __str__(self):
        return f'{self.alpha2}: {self.name}'