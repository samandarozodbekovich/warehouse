from django.db import models

from apps.shared.models import BaseTimeModel

class Product(BaseTimeModel):
    name = models.CharField(max_length=255)
    code = models.IntegerField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name