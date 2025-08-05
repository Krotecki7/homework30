from django.db import models


class Course(models.Model):
    name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Название курса"
    )
    preview = models.ImageField(
        upload_to="lms/courses", blank=True, null=True, verbose_name="Превью"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return f"{self.name}"


class Lesson(models.Model):
    name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Название урока"
    )
    preview = models.ImageField(
        upload_to="lms/courses", blank=True, null=True, verbose_name="Превью"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    video = models.URLField(
        unique=True,
        blank=True,
        null=True,
        verbose_name="Ссылка на видео",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return f"{self.name}"
