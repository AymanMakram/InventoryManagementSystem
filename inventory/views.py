from .models import Inventory
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404,redirect
from .serializers import InventoryItemSerializer
from rest_framework import generics
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import BasePermission,IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import InventoryFilter  # Import the filter class


# Custom permission class to ensure that only the owner of an object can update or delete it.
class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
    


# this function view For filtering data by category 
class InventoryListView(generics.ListAPIView):
    queryset = Inventory.objects.all()  # Get all inventory items initially
    serializer_class = InventoryItemSerializer  # Serialize the inventory items
    filter_backends = (DjangoFilterBackend,)  # Enable filtering
    filterset_class = InventoryFilter  # Use the filter class to apply filtering
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get the filter parameter from the request (category)
        queryset = super().get_queryset()  # Start with all inventory items
        
        # If there's a 'category' filter in the query params, apply the filter
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category__icontains=category)  # Filter by category
        
        return queryset

    def list(self, request, *args, **kwargs):
        # Override list to return a context for the template
        response = super().list(request, *args, **kwargs)
        # Adding context to the response
        response.data = {
            'inventory-filter': response.data,  # Add the serialized data
        }
        return response


# this function view For read all data in database and display it
class Inventory_list(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'inventory/inventory_list.html'
    permission_classes = [IsAuthenticated]

    def get(self, request):
        inventories = Inventory.objects.all()
        return Response({'inventories': inventories})


# this function view For read data per item in database and update it
class per_product(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'inventory/per_product.html'
    permission_classes = [IsAuthenticated|IsOwner]

    def get(self, request, pk):
        inventory = get_object_or_404(Inventory, pk=pk)
        # Check if the logged-in user is the owner of the inventory item
        if inventory.owner != request.user:
            raise PermissionDenied("You do not have permission to view this inventory item.")
        
        serializer = InventoryItemSerializer(inventory)
        return Response({'serializer': serializer, 'inventory': inventory})
    
    def post(self, request, pk):
        inventory = get_object_or_404(Inventory, pk=pk)
        if inventory.owner != request.user:
            raise PermissionDenied("You do not have permission to edit this inventory item.")
        
        serializer = InventoryItemSerializer(inventory, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'inventory': inventory})
        serializer.save()
        return redirect('inventory_list')

# this function view For create new inventory in database
class InventoryCreateView(generics.CreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Save the new inventory item
        serializer.save()

    def get_success_url(self):
        # This method will be called after a successful POST request
        return 'inventory_list'  # This can be a URL name for redirection

    def create(self, request, *args, **kwargs):
        # If using a form submit, this will handle POST request redirection
        response = super().create(request, *args, **kwargs)
        # Redirect to the inventory list page after creation
        return redirect('inventory_list')  # Replace 'inventory_list' with your actual URL pattern name


# this function view For delete specfic inventory in database
@login_required
def delete_inventory(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    inventory.delete()
    return redirect("/inventory/")


