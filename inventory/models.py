from django.db import models
from accounts.models import CustomUser


# Inventory Model
class Inventory(models.Model):
    CATEGORY_CHOICES = [
        ('Electronics', 'Electronics'),
        ('Clothing', 'Clothing'),
        ('Food', 'Food'),
        ('Furniture', 'Furniture'),
        ('Toys', 'Toys'),
        ('Others', 'Others'),
    ]
    
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    quantity_in_stock = models.PositiveIntegerField(null=True, blank=True)
    quantity_sold = models.PositiveIntegerField(null=False, blank=False)
    total_quantity = models.PositiveIntegerField(null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='inventory')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_added']
