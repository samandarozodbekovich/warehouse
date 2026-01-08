
from rest_framework import serializers
from apps.product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'code'
            ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at'
            ]
    
    