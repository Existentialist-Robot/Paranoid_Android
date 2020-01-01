# -*- coding: utf-8 -*-
#from django.contrib.auth.models import User, Group
from .models import Metadata
import django_filters

class MetadataFilter(django_filters.FilterSet):
#    first_name = django_filters.CharFilter(lookup_expr='icontains')
#    x_coord = django_filters.NumberFilter()
    x_coord__gt = django_filters.NumberFilter(field_name='x_coord', lookup_expr='x_coord__gt')
    x_coord__lt = django_filters.NumberFilter(field_name='x_coord', lookup_expr='x_coord__lt') 
#    y_coord = django_filters.NumberFilter()
    y_coord__gt = django_filters.NumberFilter(field_name='y_coord', lookup_expr='y_coord__gt')
    y_coord__lt = django_filters.NumberFilter(field_name='y_coord', lookup_expr='y_coord__lt') 
#    z_coord = django_filters.NumberFilter()
    z_coord__gt = django_filters.NumberFilter(field_name='z_coord', lookup_expr='z_coord__gt')
    z_coord__lt = django_filters.NumberFilter(field_name='z_coord', lookup_expr='z_coord__lt') 
    class Meta:
        model = Metadata
        fields = ['year' ,'month', 'day', ]
        
        