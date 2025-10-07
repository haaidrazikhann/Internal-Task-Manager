from rest_framework import viewsets
from .models import Team
from .serializers import TeamAdminSerializer, TeamPublicSerializer
from .permissions import IsAdminOrReadOnlyTeam


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    permission_classes = [IsAdminOrReadOnlyTeam]

    def get_serializer_class(self):
        if self.request.user and self.request.user.is_staff:
            return TeamAdminSerializer
        return TeamPublicSerializer
