from rest_framework import serializers
from .models import Course, Lesson
from .validators import validate_link


class LessonSerializer(serializers.ModelSerializer):
    video = serializers.URLField(validators=[validate_link])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(source="lesson_set", many=True, read_only=True)

    def get_count_lessons(self, obj):
        return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = ("name", "description", "count_lessons", "lessons")
