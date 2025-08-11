from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from lms.models import Course, Lesson


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Users require an email field")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="Почта")

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Укажите телефон",
    )
    city = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Город",
        help_text="Укажите город",
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="загрузите аватар",
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payments(models.Model):
    CSH = "CASH"
    CRD = "CARD"

    STATUS_CHOICE = [
        (CSH, "Оплата наличными"),
        (CRD, "Перевод на карту")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="user_set")
    date_pay = models.DateTimeField(auto_now_add=True, verbose_name="Дата платежа")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс", related_name="course_set")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Урок", related_name="lesson_set")
    amount = models.PositiveIntegerField(verbose_name="Сумма платежа", null=True, blank=True)
    payment_method = models.CharField(max_length=40, choices=STATUS_CHOICE, blank=True, null=True,
                                      verbose_name="Способ оплаты")

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"{self.user} {self.amount}"
