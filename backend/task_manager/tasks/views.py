from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from users.permissions import IsAdminOrTaskOwner


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminOrTaskOwner]
