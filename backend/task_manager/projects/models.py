from django.db import models
from django.conf import settings
from teams.models import Team  # new import

User = settings.AUTH_USER_MODEL


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    # Primary owner (creator/admin of project)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="owned_projects"
    )

    # Multiple assigned users
    assigned_users = models.ManyToManyField(
        User,
        related_name="assigned_projects",
        blank=True
    )

    # Optional assigned team
    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="projects"
    )

    def __str__(self):
        return self.name
