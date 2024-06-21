from django.urls import include, path

urlpatterns = [
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("profile/", include("account.urls")),
]
