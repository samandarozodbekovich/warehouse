from rest_framework.viewsets import ModelViewSet

from apps.product.models import Material
from apps.product.serializers import MaterialSerializer


class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    