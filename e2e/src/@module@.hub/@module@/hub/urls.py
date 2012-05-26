
from django.conf.urls import patterns, include, url
from @module@.hub import api

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ### ACCOUNTS
    url(r'^account/', include('@module@.hub.apps.accounts.urls')),

    ### ADMIN
    url(r'^admin/', include(admin.site.urls)),
    
    ### EXAMPLE
    url(r'^example/', include('@module@.hub.apps.example.urls')),
    
    ### API
    (r'^api/', include(api.v0.urls)),
    
)
