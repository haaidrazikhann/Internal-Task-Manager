# projects/views.py
from rest_framework import viewsets, permissions
from django.db.models import Q
from .models import Project
from .serializers import ProjectSerializer, ProjectNameSerializer
from .permissions import IsAdminOrReadOnlyAssigned


class ProjectViewSet(viewsets.ModelViewSet):
    """
    Permissions:
    - Admin: full CRUD.
    - Regular users: read-only for projects they own or are assigned to.
    """
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnlyAssigned]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            # Admins see everything
            return Project.objects.all()

        # Regular users: only assigned or owned projects
        return Project.objects.filter(
            Q(owner=user) | Q(assigned_users=user)
        ).distinct()

    def get_serializer_class(self):
        # Minimal data for list
        if self.action == 'list':
            return ProjectNameSerializer
        return ProjectSerializer

    def perform_create(self, serializer):
        # Owner is always the authenticated admin
        serializer.save(owner=self.request.user)
