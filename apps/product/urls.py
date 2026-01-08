
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.product.views import WarehouseViewSet, ProductMaterialViewSet, ProductViewSet, MaterialViewSet, CalculateView

router = DefaultRouter()

router.register(r'warehouses', WarehouseViewSet, basename='warehouse')
router.register(r'product-materials', ProductMaterialViewSet, basename='productmaterial')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'materials', MaterialViewSet, basename='material')


urlpatterns = [
    path('', include(router.urls)),
    path('calculate/', CalculateView.as_view(), name='calculate'),
]