import django_filters 
from .models import * 


class ReportFilter(django_filters.FilterSet):
    class Meta:
        model = Record
        fields = ['user','hour1','hour5','day']