
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.validation import FormValidation

from .. import auth
from .accounts import UserResource
from @module@.hub import forms
from @module@.hub import db

class @resource.capitalize@Resource(ModelResource):
    class Meta:
        queryset = db.@resource.capitalize@.objects.all()
        resource_name = '@plural_resource@'
        authorization = auth.@class_prefix@Authorization()
        authentication = auth.@class_prefix@Authentication()
        methods = ['get', 'put', 'post', 'delete']
        validation = FormValidation(form_class=forms.@resource_class_prefix@Form)
        
    created_by = fields.ToOneField(UserResource, 'created_by', full=True)