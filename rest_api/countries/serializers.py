from rest_framework import serializers

from countries.models import Country, Currency

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency

    def to_representation(self, instance: Currency):
        return instance.alpha3

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = [ 'id', 'alpha2', 'alpha3', 'name', 'currencies', 'deleted_date']
    
    currencies = CurrencySerializer(read_only=True, many=True)