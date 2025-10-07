from rest_framework import serializers
from .models import Project
from django.contrib.auth import get_user_model
from teams.models import Team

User = get_user_model()


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    assigned_users = serializers.SlugRelatedField(
        many=True,
        slug_field='username',
        queryset=User.objects.all()
    )
    team = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Team.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = Project
        fields = "__all__"

class ProjectNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "name")
