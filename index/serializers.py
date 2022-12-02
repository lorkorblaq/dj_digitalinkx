from rest_framework import serializers 
from .models import *

class s_and_t_serializer(serializers.ModelSerializer):
    class Meta:
        model = s_and_t, Order, OrderItem, Customer
        field = ('__all__')