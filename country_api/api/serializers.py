from models import Country, Currency
from rest_framework import serializers

# class CountrySerializer(serializers.HyperlinkedModelSerializer):

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency

    def to_representation(self, instance: Currency):
        return instance.alpha3
    
class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['alpha2', 'alpha3', 'name', 'currencies']

    currencies = CurrencySerializer(read_only=True, many=True)