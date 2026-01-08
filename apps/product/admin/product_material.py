from django.contrib import admin
from apps.product.models import ProductMaterial

@admin.register(ProductMaterial)
class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_id', 'material_id', 'quantity', 'created_at', 'updated_at']
    list_filter = ['product_id', 'material_id']
    ordering = ['-created_at']