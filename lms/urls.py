from django.urls import path

from rest_framework.routers import SimpleRouter
from lms.apps import LmsConfig
from .views import (
    CourseViewSet,
    LessonCreateApiView,
    LessonRetrieveApiView,
    LessonListApiView,
    LessonUpdateApiView,
    LessonDestroyApiView,
)

app_name = LmsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name="lessons-list"),
    path("lessons/<int:pk>/", LessonRetrieveApiView.as_view(), name="lessons-retrieve"),
    path(
        "lessons/<int:pk>/delete/",
        LessonDestroyApiView.as_view(),
        name="lessons-delete",
    ),
    path(
        "lessons/<int:pk>/update/", LessonListApiView.as_view(), name="lessons-update"
    ),
    path("lessons/create/", LessonCreateApiView.as_view(), name="lessons-create"),
] + router.urls
