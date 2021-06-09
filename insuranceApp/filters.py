import django_filters
from django_filters import *
from .models import *

class LocationFilter(django_filters.FilterSet):
    class Meta:
        model = Location
        fields = "__all__"
        exclude = ('name', 'address', 'phone', 'workDate', 'workClock', 'mapLocation')
    

class ContactFilter(django_filters.FilterSet):
    class Meta:
        model = Contact
        fields = "__all__"
        excude = ("name", "phone", "description", "create_date")  




