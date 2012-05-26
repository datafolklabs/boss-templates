
from django import forms
from @module@.hub import db

class ExampleForm(forms.ModelForm):
    class Meta:
        model = db.Example