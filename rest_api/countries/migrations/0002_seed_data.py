# Generated by Django 5.0.4 on 2024-05-01 11:42

from django.db import migrations

def populate_countries(apps, schema_editor):
    Country = apps.get_model('countries', 'Country')

    raw_data = [
        { 'name': 'united kingdom', 'alpha2': 'gb', 'alpha3': 'gbr', 'number3': '826', 'currencies': [ 'gbp', 'usd' ]},
        { 'name': 'south africa', 'alpha2': 'za', 'alpha3': 'zaf', 'number3': '710', 'currencies': [ 'zar', 'usd' ]},
        { 'name': 'eswatini', 'alpha2': 'sz', 'alpha3': 'swz', 'number3': '748', 'currencies': [ 'zar', 'usd', 'szl', 'mzn' ]},
        { 'name': 'mozambique', 'alpha2': 'mz', 'alpha3': 'moz', 'number3': '508', 'currencies': [ 'usd', 'mzn' ]},
        { 'name': 'zimbabwe', 'alpha2': 'zw', 'alpha3': 'zwe', 'number3': '716', 'currencies': [ 'zar', 'usd', 'zwl' ]},
    ]

    for raw in raw_data:
        country = Country(
            name=raw['name'],
            alpha2=raw['alpha2'],
            alpha3=raw['alpha3'],
            number3=raw['number3'],
            currencies=raw['currencies']
        )
        country.save()


def undo(apps, schema_editor):

    Country = apps.get_model('countries', 'Country')
    Country.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_countries, undo),
    ]
