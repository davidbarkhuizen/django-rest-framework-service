from models import Country
from rest_framework import serializers

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ['alpha2', 'alpha3', 'name', 'currencies']
