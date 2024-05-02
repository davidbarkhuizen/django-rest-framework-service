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

    def get_queryset(self):

        query = Country.objects.exclude(deleted_date__isnull=False)

        query = query.order_by('alpha2')

        return query

    def retrieve(self, request, pk):

        if len(pk) not in [2, 3]:
            return Response(status = 400) # bad request

        target = Country.objects.get(alpha2=pk) if len(pk) == 2 else Country.objects.get(alpha3=pk)
                
        return Response(
            CountrySerializer(
                target
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
