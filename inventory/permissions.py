from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an inventory item to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are granted to all users
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the owner of the object
        return obj.owner == request.user