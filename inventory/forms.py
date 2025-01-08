from django.forms import ModelForm
from .models import Inventory

class AddInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'description', 'quantity_sold','total_quantity','price','category','owner']


# class UpdateInventoryForm(ModelForm):
#     class Meta:
#         model = Inventory
#         fields = ['name', 'description', 'quantity', 'price','category','owner']