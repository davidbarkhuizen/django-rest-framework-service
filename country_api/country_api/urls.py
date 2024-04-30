from django.contrib import admin
from django.urls import path, include, re_path

from api import urls as api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'.*', include(api_urls)),
]
