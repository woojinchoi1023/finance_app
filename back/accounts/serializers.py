from rest_framework import serializers
from .models import User
from finance.models import User_Product

class UserSerializer(serializers.ModelSerializer):
    class UserProductSerialzier(serializers.ModelSerializer):
        class Meta:
            model = User_Product
            fields = '__all__'
    user_product_set = UserProductSerialzier(read_only=True, many=True)
    class Meta:
        model = User
        fields = '__all__'



    