from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "toggl_api_key",
            "workspace_id",
            "project_id",
            "tags",
        )


class AccountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("toggl_api_key", "workspace_id", "project_id", "tags")
