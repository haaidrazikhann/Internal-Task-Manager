from django.db import models
from django.conf import settings
from projects.models import Project

User = settings.AUTH_USER_MODEL


class Task(models.Model):
    STATUS_CHOICES = (
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo")

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    # Multiple assignees instead of one
    assigned_users = models.ManyToManyField(
        User,
        related_name="tasks",
        blank=True
    )

    due_date = models.DateField(null=True, blank=True)

    @property
    def overdue(self):
        from django.utils import timezone
        return self.due_date and self.due_date < timezone.now().date() and self.status != "done"

    def __str__(self):
        return self.title
