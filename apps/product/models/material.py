from django.db import models

from apps.product.models.product import Product
from apps.shared.models import BaseTimeModel

class Material(BaseTimeModel):

    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name