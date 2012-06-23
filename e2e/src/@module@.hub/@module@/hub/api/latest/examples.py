
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.validation import FormValidation

from @module@.hub import forms
from @module@.hub import db
from @module@.hub.api import auth
from .accounts import UserResource

class ExampleResource(ModelResource):
    class Meta:
        queryset = db.Example.objects.all()
        resource_name = 'examples'
        authorization = auth.@class_prefix@Authorization()
        authentication = auth.@class_prefix@Authentication()
        methods = ['get', 'put', 'post', 'delete']
        validation = FormValidation(form_class=forms.ExampleForm)
        
    created_by = fields.ToOneField(UserResource, 'created_by', full=True)