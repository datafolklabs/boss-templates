
from django.conf.urls import patterns, include, url

urlpatterns = patterns('@module@.hub.apps.examples.views',
    url(r'^$', 'index', name='examples_index'),
    url(r'^manage/$', 'manage', name='manage_examples'),
    url(r'^create/$', 'create', name='create_example'),
    url(r'^(?P<example_id>)/$', 'details', name='example_details'),
    url(r'^update/(?P<example_id>)/$', 'update', name='update_example'),
    url(r'^delete/(?P<example_id>)/$', 'delete', name='delete_example'),
)
