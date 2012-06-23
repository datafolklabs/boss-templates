
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.validation import FormValidation

from @module@.hub import forms
from @module@.hub import db
from @module@.hub.api import auth
from .accounts import UserResource

class @resource.capitalize@Resource(ModelResource):
    class Meta:
        queryset = db.@resource.capitalize@.objects.all()
        resource_name = '@plural_resource@'
        authorization = auth.@class_prefix@Authorization()
        authentication = auth.@class_prefix@Authentication()
        methods = ['get', 'put', 'post', 'delete']
        validation = FormValidation(form_class=forms.@resource.capitalize@Form)
        
    created_by = fields.ToOneField(UserResource, 'created_by', full=True)