from django.urls import path
from .views import Inventory_list,per_product,delete_inventory,InventoryCreateView, InventoryListView


urlpatterns = [
    # main inventory page
    path('', Inventory_list.as_view(), name="inventory_list"),
    # details each item page
    path('per_product/<int:pk>/', per_product.as_view(template_name = 'inventory/per_product.html'), name="per_product"),
    # add invetory form page
    path('add_inventory/', InventoryCreateView.as_view(), name='inventory-create'),
    # delete url
    path('delete/<int:pk>', delete_inventory, name="delete_inventory"),
    path('api/filter/', InventoryListView.as_view(), name='inventory-filter'),
    
]



