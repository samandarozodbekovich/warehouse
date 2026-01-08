from rest_framework.viewsets import ModelViewSet

from apps.product.models import Warehouse
from apps.product.serializers import WarehouseSerializer


class WarehouseViewSet(ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer