import django
from django.urls import include, path, re_path
from django.contrib import admin

admin.autodiscover()


urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]


if django.VERSION < (1, 9, 0):
    urlpatterns += [path("admin/", include(admin.site.urls))]
else:
    urlpatterns += [re_path(r"^admin/", admin.site.urls)]
