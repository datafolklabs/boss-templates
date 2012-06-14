
from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from @module@.hub import api

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ### MAIN INDEX
    url('^$', direct_to_template, {'template': 'index.html'}, name='index'),
        
    ### ACCOUNTS
    url(r'^account/', include('@module@.hub.apps.accounts.urls')),

    ### ADMIN
    url(r'^admin/', include(admin.site.urls)),
    
    ### EXAMPLE APP
    url(r'^examples/', include('@module@.hub.apps.examples.urls')),
    
    ### API
    (r'^api/', include(api.v0.urls)),
    
)
