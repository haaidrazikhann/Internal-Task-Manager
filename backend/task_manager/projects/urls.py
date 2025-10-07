from django.urls import path
from .views import ProjectViewSet

project_list = ProjectViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

project_detail = ProjectViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', project_list, name='project-list'),
    path('<int:pk>/', project_detail, name='project-detail'),
]
