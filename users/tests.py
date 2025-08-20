from rest_framework.test import APITestCase
from lms.models import Course
from .models import Follow, User
from django.urls import reverse
from rest_framework import status


class FollowTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@admin.com")
        self.course = Course.objects.create(
            name="Джанго", description="Уроки по Джанго", owner=self.user
        )
        self.follow = Follow.objects.create(course=self.course, user=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscription(self):
        url = reverse("users:follow_check")
        data = {"course_id": self.course.pk}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("message"), "Subscription removed")
