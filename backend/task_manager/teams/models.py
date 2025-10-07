from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(User, related_name="teams", blank=True)

    def __str__(self):
        return self.name
