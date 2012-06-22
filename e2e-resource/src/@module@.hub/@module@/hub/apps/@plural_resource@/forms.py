
from django import forms
from @module@.hub import db

class @resource_class_prefix@Form(forms.ModelForm):
    class Meta:
        model = db.@resource.capitalize@