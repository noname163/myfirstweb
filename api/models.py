from django.db import models
from tastypie.resources import ModelResource
from information.models import Tree

class InforResource(ModelResource):
    class Meta:
        queryset= Tree.objects.all()
        resource_name= 'information'