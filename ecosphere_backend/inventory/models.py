from django.db import models

# Create your models here.
class UserAction(models.Model):
    ACTION_CHOICES = [
        ("recycled", "Recycled"),
        ("reused", "Reused"),
        ("donated", "Donated"),
        ("discarded", "Discarded"),
        ("expired", "Expired"),
    ]

    inventory_item = models.ForeignKey(
        InventoryItem,
        on_delete=models.CASCADE,
        related_name="actions"
    )

    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    points_awarded = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
