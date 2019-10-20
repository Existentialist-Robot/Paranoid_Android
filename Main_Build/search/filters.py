# -*- coding: utf-8 -*-
#from django.contrib.auth.models import User, Group
from . import models.Metadata as Metadata
import django_filters

class MetadataFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Metadata
        fields = ['username', 'first_name', 'last_name', ]