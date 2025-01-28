from django.urls import path, include
from wagtail import urls as wagtail_urls

urlpatterns = [
    path('', include(wagtail_urls)),
]