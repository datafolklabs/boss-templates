
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.validation import FormValidation
from @module@.hub.api.version0 import auth
from @module@.hub import forms
from @module@.hub import db

class @resource_class_prefix@Resource(ModelResource):
    class Meta:
        queryset = db.@resource_class_prefix@.objects.all()
        resource_name = '@plural_resource@'
        authorization = auth.@class_prefix@Authorization()
        authentication = auth.@class_prefix@Authentication()
        methods = ['get', 'put', 'post', 'delete']
        validation = FormValidation(form_class=forms.@resource_class_prefix@Form)
        
    created_by = fields.ToOneField(UserResource, 'created_by', full=True)