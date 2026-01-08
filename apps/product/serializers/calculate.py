from genericpath import exists
from rest_framework.validators import ValidationError
from rest_framework import serializers

from apps.product.models.product import Product


class CalculateSerializer(serializers.Serializer):
    
    code = serializers.IntegerField()
    quantity = serializers.IntegerField()
    
    def validate_quantity(self, value):
        if value < 0:
            raise ValidationError({
                "message":"Quantity must be greater than 0"
            })
        return value
    
    def validate_code(self, value):
        if not Product.objects.filter(code=value).exists():
            raise ValidationError({
                "message":f"Product with {value} does not exist."
            })
        return value
            
    