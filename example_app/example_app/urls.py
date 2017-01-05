import sys, os
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
import django.views.static
sys.path.insert(0, os.path.abspath('..'))
import cms.urls as cms_urls
import crowdsourcing.urls
admin.autodiscover()

urlpatterns = [
    url('', include(cms_urls)),
    url(r'^crowdsourcing/', include(crowdsourcing.urls)),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$',
     django.views.static.serve,
     {'document_root': settings.MEDIA_ROOT}),
    # See settings.py for detailed instructions on how to build the
    # documentation.
    url(r'^docs/(?P<path>.*)$',
     django.views.static.serve,
     {'document_root': settings.DOCUMENTATION_ROOT})
]

from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)