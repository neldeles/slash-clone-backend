from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models
from fernet_fields import EncryptedTextField


class CustomUser(AbstractUser):
    toggl_api_key = EncryptedTextField(blank=True, null=True)
    workspace_id = models.IntegerField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    tags = ArrayField(models.CharField(max_length=80), blank=True, null=True)
