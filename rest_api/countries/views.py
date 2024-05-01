from rest_framework import viewsets
from countries.models import Country
from countries.serializers import CountrySerializer

class CountryViewSet(viewsets.ModelViewSet):

    queryset = Country.objects.all().order_by('-alpha2')
    serializer_class = CountrySerializer


