from django.db import models

from apps.product.models.material import Material
from apps.shared.models import BaseTimeModel


class Warehouse(BaseTimeModel):
    material = models.ForeignKey(
        Material, on_delete=models.SET_NULL, null=True, blank=True
    )
    remainder = models.PositiveIntegerField()
    price = models.IntegerField()
    
    def __str__(self):
        return f"Warehouse Material ID: {self.material}, Remainder: {self.remainder}, Price: {self.price}"