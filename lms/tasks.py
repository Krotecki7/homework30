from celery import shared_task
from config.settings import EMAIL_HOST_USER
from .models import Course
from users.models import Follow, User
from django.core.mail import send_mail


@shared_task
def send_notification(course_pk):
    course = Course.objects.filter(pk=course_pk).first()
    users = User.objects.all()
    for user in users:
        follow = Follow.objects.filter(course=course.pk, user=user.pk).first()
        if follow:
            send_mail(
                "Обновление курса из вашей подписки",
                "Курс из вашей подписки был обновлен",
                EMAIL_HOST_USER,
                [user.email],
            )
