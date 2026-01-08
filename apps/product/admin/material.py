from django.contrib import admin
from apps.product.models import Material

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at']
    list_filter = ['name']
    ordering = ['-created_at']