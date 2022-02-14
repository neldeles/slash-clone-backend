from django.urls import path
from .views import ListTodo, DetailTodo

urlpatterns = [
    path("<str:pk>/", DetailTodo.as_view(), name="task-detail"),
    path("", ListTodo.as_view(), name="tasks"),
]
