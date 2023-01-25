from rest_framework import serializers
from .models import Order, Comment

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__' 

