from rest_framework import serializers
from apps.product.models import ProductMaterial
from apps.product.serializers.material import MaterialSerializer
from apps.product.serializers.product import ProductSerializer

class ProductMaterialSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductMaterial
        fields = [
            'id',
            'product',
            'material',
            'quantity'
            ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at'
            ]
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['product'] = ProductSerializer(instance.product).data
        data['material'] = MaterialSerializer(instance.material).data
        return data