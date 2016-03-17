from django.db import models
from django.utils import timezone

class Supplie(models.Model):
    inventory_number = models.IntegerField()
    product_name = models.CharField(max_length=200)
    supplier = models.CharField(max_length=200)
    catalog_number = models.CharField(max_length=200)
    quantity_present = models.IntegerField()
    
    def __str__(self):
        return self.product_name