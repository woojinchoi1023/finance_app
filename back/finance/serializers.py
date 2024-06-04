from rest_framework import serializers
from .models import Exchangerate
from .models import Product, User_Product

class ExchangerateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exchangerate
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        

class SubscribeSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    class Meta:
        model = User_Product
        fields = '__all__'
        read_only_fields = ('user', )