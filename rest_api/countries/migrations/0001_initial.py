# Generated by Django 5.0.4 on 2024-05-02 09:35

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alpha2', models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')])),
                ('alpha3', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')])),
                ('deleted_date', models.DateTimeField(default=None, null=True)),
                ('name', models.CharField(max_length=100)),
                ('numeric3', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator('^[0-9]*$', 'Only numeric characters are allowed.')])),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scale', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('alpha3', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')])),
                ('numeric3', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator('^[0-9]*$', 'Only numeric characters are allowed.')])),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CountryCurrencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countries.country')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countries.currency')),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='currencies',
            field=models.ManyToManyField(through='countries.CountryCurrencies', to='countries.currency'),
        ),
    ]
