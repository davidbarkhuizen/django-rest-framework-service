from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.response import Response
from countries.models import Country
from countries.serializers import CountrySerializer
from django.utils.timezone import now

class CountryViewSet(viewsets.ModelViewSet):

    serializer_class = CountrySerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = [ 'currencies__alpha3' ]

    #search_fields = [ 'currencies_alpha3' ]

    def get_queryset(self):

        query = Country.objects.exclude(deleted_date__isnull=False)

        query = query.order_by('alpha2')

        return query

    def retrieve(self, request, pk=None):
                
        return Response(
            CountrySerializer(
                Country.objects.get(pk=pk)
            ).data
        )   

    def destroy(self, request, pk=None):
        
        target = None
        try:
            target = Country.objects.get(pk=pk)
        except:
            return Response(status=404) # not found

        if target.deleted_date is not None:
            return Response(status=410) # gone
    
        target.deleted_date = now()
        target.save()

        return Response(status=204) # operation success, no content
