from django.urls import path

from account.views import Verification

urlpatterns = [
    path("", Verification.as_view(), name="Hello authentication"),
]
