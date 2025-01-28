from django.urls import path, include
from wagtail import urls as wagtail_urls
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
