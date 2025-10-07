from rest_framework.permissions import BasePermission


class IsAdminOrReadOnlyTeam(BasePermission):
    """
    Admins: full CRUD
    Non-admins: read-only (but restricted fields in serializer)
    """

    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True
        if view.action in ["list", "retrieve"]:
            return True
        return False
