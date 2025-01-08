import django_filters
from .models import Inventory  # Import your model

class InventoryFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category', lookup_expr='icontains', label='Category')

    class Meta:
        model = Inventory
        fields = ['category']  # Add other fields if needed
