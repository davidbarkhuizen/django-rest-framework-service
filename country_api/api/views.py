

from rest_framework import permissions, viewsets

from country_api.api.models import Country
from country_api.api.serializers import CountrySerializer

class CountryViewSet(viewsets.ModelViewSet):

    queryset = Country.objects.all().order_by('-alpha2')
    serializer_class = CountrySerializer
    permission_classes = []

