
from django import forms
from @module@.hub import db

class @resource.capitalize@Form(forms.ModelForm):
    class Meta:
        model = db.@resource.capitalize@