from django.contrib import admin
from apps.product.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 'created_at', 'updated_at']
    list_filter = ['name', 'code']
    ordering = ['-created_at']
    
    