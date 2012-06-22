
from django.conf.urls import patterns, include, url

urlpatterns = patterns('@module@.hub.apps.@plural_resource@.views',
    url(r'^$', 'index', name='@plural_resource@_index'),
    url(r'^manage/$', 'manage', name='manage_@plural_resource@'),
    url(r'^create/$', 'create', name='create_@resource@'),
    url(r'^(?P<@resource@_id>)/$', 'details', name='@resource@_details'),
    url(r'^update/(?P<@resource@_id>)/$', 'update', name='update_@resource@'),
    url(r'^delete/(?P<@resource@_id>)/$', 'delete', name='delete_@resource@'),
)
