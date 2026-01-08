from rest_framework import serializers
from apps.product.models import Material

class MaterialSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Material
        fields = [
            'id',
            'name',
            ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at'
            ]