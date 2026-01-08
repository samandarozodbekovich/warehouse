from django.contrib import admin
from apps.product.models import Warehouse

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'material_id', 'remainder', 'price', 'created_at', 'updated_at']
    list_filter = ['material_id']
    ordering = ['-created_at']
