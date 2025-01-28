from django.contrib import admin
from django.urls import path, include
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail import urls as wagtail_urls

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # Wagtail CMS
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    # Apps
    path('news/', include('apps.news.urls')),

    # Wagtail Frontend
    path('', include(wagtail_urls)),
]
