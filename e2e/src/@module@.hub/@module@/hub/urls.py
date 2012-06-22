
from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from @module@.hub import api

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ### MAIN INDEX
    url('^$', direct_to_template, {'template': 'index.html'}, name='index'),
    
    ### APPS
    url(r'^account/', include('@module@.hub.apps.accounts.urls')),
    url(r'^examples/', include('@module@.hub.apps.examples.urls')),
    # @boss.mark:url_ref@
            
    ### ADMIN
    url(r'^admin/', include(admin.site.urls)),
    
    ### API
    (r'^api/', include(api.v0.urls)),

)
