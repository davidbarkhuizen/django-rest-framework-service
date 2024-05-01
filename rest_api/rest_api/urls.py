from django.urls import include, path
from rest_framework import routers

from countries import views

router = routers.DefaultRouter()
router.register(r'countries', views.CountryViewSet, basename='Countries')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]