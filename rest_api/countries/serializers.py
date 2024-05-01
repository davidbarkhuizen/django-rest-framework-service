from rest_framework import serializers

from countries.models import Country
    
class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['alpha2', 'alpha3', 'name', 'currencies']