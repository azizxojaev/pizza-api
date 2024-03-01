from rest_framework.serializers import ModelSerializer
from .models import *
from datetime import datetime


class MenuSerializer(ModelSerializer):
    
    class Meta:
        model = Pizza
        exclude = ['id']


class ProductSerializer(ModelSerializer):
    
    class Meta:
        model = Pizza
        fields = ['name']


class OrdersSerializer(ModelSerializer):
    products = ProductSerializer(many=True)
    
    class Meta:
        model = Order
        fields = '__all__'
        
    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata['created'] = datetime.strftime(instance.created, '%d-%m-%Y %H:%M:%S')
        return redata
    
