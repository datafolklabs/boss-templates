
from django.conf.urls import patterns, include, url

urlpatterns = patterns('@module@.hub.apps.example.views',
    url(r'^$', 'index', name='example_index'),
)
