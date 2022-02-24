from django.urls import path
from .views import AccountUpdateView, AccountDetailView

urlpatterns = [
    path("update/<int:pk>/", AccountUpdateView.as_view(), name="account-update"),
    path("<int:pk>/", AccountDetailView.as_view(), name="account-list"),
]
