from rest_framework import serializers
from apps.product.models import Warehouse

class WarehouseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Warehouse
        fields = [
            'id',
            'material_id',
            'remainder',
            'price',
            ]
        read_only_fields = [
            'id',
            'material_id',
            'created_at',
            'updated_at'
            ]