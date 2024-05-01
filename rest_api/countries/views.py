from rest_framework import viewsets
from rest_framework.response import Response
from countries.models import Country
from countries.serializers import CountrySerializer
from django.utils.timezone import now

class CountryViewSet(viewsets.ModelViewSet):

    def list(self, request):

        query = Country.objects.exclude(deleted_date__isnull=False)

        matching_currency = request.query_params.get('currency', None)
        if matching_currency is not None:
            matching_currency = matching_currency.lower()
                
        if matching_currency:
            query = query.filter(currencies__contains=matching_currency)

        query = query.order_by('-alpha2')
        
        serializer = CountrySerializer(query, many=True)
        
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        return Response(
            CountrySerializer(
                Country.get(pk=pk)
            ).data
        )   

    def destroy(self, request, pk=None):
        
        target = Country.get(pk=pk)
        
        if target.deleted_date is not None:
    
            target.deleted_date = now()
            target.save()

            return Response()

