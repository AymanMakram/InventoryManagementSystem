from rest_framework import serializers
from .models import Inventory


class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'name', 'description','quantity_sold', 'total_quantity', 'price', 'category', 'date_added', 'last_updated','owner']
        read_only_fields = ['owner']  # Make owner read-only to prevent modification after creation

    def validate(self, attrs):
        # Automatically set owner from logged-in user if it's not already set
        if 'owner' not in attrs and self.context.get('request') is not None:
            attrs['owner'] = self.context['request'].user  # Access the logged-in user
            
        # Get the current total quantity if updating, otherwise use the quantity passed in the request.
        if self.instance:
            # For updates, get the current `total_quantity` from the instance.
            total_quantity = self.instance.total_quantity if self.instance else 0
        else:
            # If this is a new object, make sure the `total_quantity` is included in `attrs`.
            total_quantity = attrs.get('total_quantity', 0)

        # Get quantity to be sold from the request data.
        quantity_sold = attrs.get('quantity_sold', 0)
        
        # Calculate remaining stock after sale.
        quantity_in_stock = total_quantity - quantity_sold

        # Check if there is any increase in the total_quantity.
        new_total_quantity = attrs.get('total_quantity', total_quantity)
        if new_total_quantity > total_quantity:
            # If total_quantity is increased, update quantity_in_stock accordingly.
            quantity_in_stock = self.instance.quantity_in_stock + (new_total_quantity - total_quantity) if self.instance else new_total_quantity


                # Check if there is any increase in the total_quantity.
        new_total_quantity = attrs.get('total_quantity', total_quantity)
        if new_total_quantity < total_quantity:
            # If total_quantity is increased, update quantity_in_stock accordingly.
            quantity_in_stock = self.instance.quantity_in_stock - (total_quantity - new_total_quantity) if self.instance else new_total_quantity

        # Check if remaining stock is negative.
        if quantity_in_stock < 0:
            raise serializers.ValidationError("Not enough inventory to sell this amount.")
        
        # Set the updated `quantity_in_stock` value.
        attrs['quantity_in_stock'] = quantity_in_stock
        
        return attrs
