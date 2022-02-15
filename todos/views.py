from rest_framework import generics
from .models import Task
from .permissions import IsUser
from .serializers import TaskSerializer, TaskCreateSerializer
from django.contrib.auth import get_user_model

import datetime


class TaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        This view should return a list of all the tasks
        for the currently authenticated user.
        """
        user = self.request.user
        print(user)
        return Task.objects.filter(user=user)


class TaskDetailView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsUser,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskUpdateView(generics.UpdateAPIView):
    permission_classes = (IsUser,)
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer

    def perform_update(self, serializer):
        if self.request.data["status"] == "DONE":
            serializer.save(date_done=datetime.datetime.now())
        else:
            serializer.save(date_done=None)


class TaskDeleteView(generics.DestroyAPIView):
    permission_classes = (IsUser,)
    queryset = Task.objects.all()
