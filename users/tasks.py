from .models import User
from celery import shared_task
from django.utils import timezone


@shared_task
def deactivated():
    today = timezone.now().today().date()
    users = User.objects.filter(
        last_login__isnull=False, last_login__lt=today - timezone.timedelta(days=30)
    )
    if users:
        for user in users:
            user.is_active(False)
            user.save()
