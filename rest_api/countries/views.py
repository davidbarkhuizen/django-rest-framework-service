from rest_framework import viewsets
from rest_api.countries.models import Country
from rest_api.countries.serializers import CountrySerializer

class CountryViewSet(viewsets.ModelViewSet):

    queryset = Country.objects.all().order_by('-alpha2')
    serializer_class = CountrySerializer
    permission_classes = []

