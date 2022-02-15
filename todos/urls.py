from django.urls import path
from .views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)

urlpatterns = [
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("delete/<str:pk>/", TaskDeleteView.as_view(), name="task-detail"),
    path("update/<str:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("<str:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("", TaskListView.as_view(), name="task-list"),
]
