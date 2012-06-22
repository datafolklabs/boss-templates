
from django.db import models
from django.contrib.auth.models import User

class @resource_class_prefix@(models.Model):
    class Meta:
        db_table = '@plural_resource@'
        ordering = ['label']

    created_by = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True, auto_now=True)
    label = models.CharField(max_length=128, blank=False, unique=True)