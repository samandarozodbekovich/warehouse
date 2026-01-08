from rest_framework.viewsets import ModelViewSet

from apps.product.models import ProductMaterial
from apps.product.serializers import ProductMaterialSerializer


class ProductMaterialViewSet(ModelViewSet):
    queryset = ProductMaterial.objects.all()
    serializer_class = ProductMaterialSerializer