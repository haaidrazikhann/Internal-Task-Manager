from rest_framework import permissions


class IsAdminOrTaskOwner(permissions.BasePermission):
    """
    Admins: Full CRUD
    Members: Can read & update only their own tasks
    """

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Admins can do anything
        if user.role == "admin":
            return True

        # Members can read and update their own tasks only
        if user.role == "member":
            if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
                return True
            if request.method in ["PUT", "PATCH"]:
                return obj.assigned_to == user

        # Otherwise, deny
        return False
