
from django.conf.urls import patterns, include, url

urlpatterns = patterns('@module@.hub.apps.accounts.views',
    url(r'', include('userena.urls')),
)
