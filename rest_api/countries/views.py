from rest_framework import viewsets
from rest_framework.response import Response
from countries.models import Country
from countries.serializers import CountrySerializer
from django.utils.timezone import now

def list_countries_query(currency_alpha3: str = None):

    query = Country.objects.exclude(deleted_date__isnull=False)

    if currency_alpha3 is not None:
        currency_alpha3 = currency_alpha3.lower()

    if currency_alpha3:
        query = query.filter(currencies__alpha3=currency_alpha3)

    query = query.order_by('-alpha2')

    return query

class CountryViewSet(viewsets.ModelViewSet):

    def list(self, request):

        currency_filter = request.query_params.get('currency', None)
        q = list_countries_query(currency_filter)

        serializer = CountrySerializer(q, many=True)
        
        return Response(serializer.data)

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
