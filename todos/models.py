import uuid

from django.db import models
from django.contrib.auth import get_user_model
from model_utils.models import TimeStampedModel

User = get_user_model()

STATUS_CHOICES = (
    ("THIS_WEEK", "This Week"),
    ("DONE", "Done"),
    ("TODAY", "Today"),
)


class Task(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task = models.CharField(max_length=140)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    date_done = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.task
