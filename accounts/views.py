from rest_framework import generics
from .permissions import IsUser
from .serializers import AccountUpdateSerializer, AccountDetailSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountDetailView(generics.RetrieveAPIView):
    permission_classes = (IsUser,)
    queryset = User.objects.all()
    serializer_class = AccountDetailSerializer


class AccountUpdateView(generics.UpdateAPIView):
    permission_classes = (IsUser,)
    queryset = User.objects.all()
    serializer_class = AccountUpdateSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs["partial"] = True
        print(self.request)
        return super(AccountUpdateView, self).get_serializer(*args, **kwargs)
