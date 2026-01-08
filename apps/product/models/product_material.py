
from django.db import models
from django.core.validators import MinValueValidator

from apps.product.models.product import Product
from apps.product.models.material import Material
from apps.shared.models import BaseTimeModel

class ProductMaterial(BaseTimeModel):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.FloatField(validators=[MinValueValidator(0.0)])
    
    def __str__(self):
        return f"Product: {self.product}, Material: {self.material}, Quantity: {self.quantity}"