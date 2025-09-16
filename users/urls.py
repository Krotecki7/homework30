from django.urls import path
from rest_framework.permissions import AllowAny
from users.apps import UsersConfig
from .views import (
    UserCreateAPIView,
    UserDestroyAPIView,
    UserUpdateAPIView,
    UserRetrieveAPIView,
    FollowAPIView,
    PaymentsCreateAPIView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("<int:pk>/", UserRetrieveAPIView.as_view(), name="user_detail"),
    path("<int:pk>/delete", UserDestroyAPIView.as_view(), name="user_delete"),
    path("<int:pk>/update", UserUpdateAPIView.as_view(), name="user_update"),
    path("follow/", FollowAPIView.as_view(), name="follow_check"),
    path("payments/", PaymentsCreateAPIView.as_view(), name="payments"),
]
