# projects/permissions.py
from rest_framework import permissions

class IsAdminOrReadOnlyAssigned(permissions.BasePermission):
    """
    - Admins can do anything.
    - Regular users can only view projects they are part of (read-only).
    """

    def has_permission(self, request, view):
        # Allow safe methods (GET, HEAD, OPTIONS) for authenticated users
        if request.method in permissions.SAFE_METHODS and request.user.is_authenticated:
            return True

        # Allow all methods for admin/staff
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # Admins can do anything
        if request.user.is_staff:
            return True

        # Regular users can only read if they are owner or assigned
        if request.method in permissions.SAFE_METHODS:
            return (obj.owner == request.user) or (request.user in obj.assigned_users.all())

        # Deny write/delete for non-admins
        return False
