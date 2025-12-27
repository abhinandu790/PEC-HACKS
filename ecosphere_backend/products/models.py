from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class InventoryItem(models.Model):
    product_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255)

    quantity = models.CharField(max_length=100)
    packaging = models.CharField(max_length=255)
    packaging_tags = models.JSONField(default=list)

    eco_score = models.IntegerField()
    image = models.URLField(blank=True)

    expiry_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def days_left(self):
        return (self.expiry_date - timezone.now().date()).days

    def __str__(self):
        return self.product_name
