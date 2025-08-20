from rest_framework import serializers
from .models import Course, Lesson
from .validators import validate_link
from users.serializers import FollowSerializer


class LessonSerializer(serializers.ModelSerializer):
    video = serializers.URLField(validators=[validate_link])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(source="lesson_set", many=True, read_only=True)
    follow = serializers.SerializerMethodField()

    def get_count_lessons(self, obj):
        return obj.lesson_set.count()

    def get_follow(self, obj):
        return self.context["request"].user.user_follow.filter(course=obj).exists()

    class Meta:
        model = Course
        fields = (
            "name",
            "description",
            "count_lessons",
            "lessons",
            "follow",
        )
