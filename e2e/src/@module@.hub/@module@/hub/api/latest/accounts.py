
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.validation import FormValidation

from @module@.hub import forms
from @module@.hub import db
from @module@.hub.api import auth

class ProfileResource(ModelResource):
    class Meta:
        authentication = auth.@class_prefix@Authentication()
        authorization = auth.@class_prefix@Authorization()
        queryset = db.Profile.objects.all()
        resource_name = 'profiles'
        methods = ['get']
        
class UserResource(ModelResource):
    class Meta:
        authentication = auth.@class_prefix@Authentication()
        authorization = auth.@class_prefix@Authorization()
        queryset = db.User.objects.all()
        resource_name = 'users'
        excludes = [
            'email',
            'password',
            'is_superuser',
            ]
        methods = ['get']

    profile = fields.ToOneField(ProfileResource, 'profile', full=True)
