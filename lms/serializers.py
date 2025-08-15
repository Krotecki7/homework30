from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()
    lessons = LessonSerializer(source="lesson_set", many=True, read_only=True)

    def get_count_lessons(self, obj):
        return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = ("name", "description", "count_lessons", "lessons")
