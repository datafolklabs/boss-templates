
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.validation import FormValidation
from @module@.hub.api.version0 import auth
from @module@.hub import forms
from @module@.hub import db

class ProfileResource(ModelResource):
    class Meta:
        authentication = auth.@class_prefix@Authentication()
        authorization = auth.@class_prefix@Authorization()
        queryset = db.Profile.objects.all()
        resource_name = 'profiles'
        methods = ['get']