from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    get_object_or_404,
)
from rest_framework.permissions import AllowAny
from .models import Payments, User, Follow
from .serializers import PaymentsSerializers, UserSerializer, FollowSerializer
from lms.models import Course


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializers
    filterset_fields = ["course", "lesson", "payment_method"]
    ordering_fields = ["date_pay"]


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class FollowUpdateAPIView(UpdateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("id")
        course_item = get_object_or_404(Course, id=course_id)

        subs_item = Follow.objects.filter(user=user, courses=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = "подписка удалена"
            status_code = status.HTTP_200_OK
        else:
            subs_item.create()
            message = "подписка добавлена"
            status_code = status.HTTP_201_CREATED

        return Response({"message": message}, status=status_code)
