from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects.views import ProjectViewSet
from tasks.views import TaskViewSet
from teams.views import TeamViewSet
from users.views import UserViewSet  # ✅ add this import

# Main DRF router
router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'users', UserViewSet, basename='user')  # ✅ register users here

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT Authentication endpoints
    path('api/users/', include('users.urls')),  # login + token refresh
    path('api/projects/', include('projects.urls')), 

    # API ViewSets
    path('api/', include(router.urls)),
]
