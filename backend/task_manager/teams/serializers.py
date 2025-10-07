from rest_framework import serializers
from .models import Team
from users.serializers import UserSerializer  # reuse existing serializer


class TeamAdminSerializer(serializers.ModelSerializer):
    """Full CRUD serializer for admins — shows full user details"""
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ["id", "name", "members"]


class TeamPublicSerializer(serializers.ModelSerializer):
    """Public view for non-admins — only username + role of members"""
    members = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ["id", "name", "members"]

    def get_members(self, obj):
        return [
            {"username": member.username, "role": member.role}
            for member in obj.members.all()
        ]
