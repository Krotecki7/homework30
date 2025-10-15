from rest_framework.views import APIView
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
from rest_framework.response import Response
from .services import create_price, create_stripe_session, create_product


class PaymentsCreateAPIView(CreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializers

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        product = create_product(payment)
        price = create_price(payment.amount, product)
        session_id, payment_link = create_stripe_session(price)
        payment.session_id = session_id
        payment.payment_link = payment_link
        payment.save()


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


class FollowAPIView(APIView):
    def post(self, request):
        user = request.user
        course_id = request.data.get("course_id")
        course = get_object_or_404(Course, id=course_id)

        subscription, created = Follow.objects.get_or_create(user=user, course=course)
        print(subscription)
        if not created:
            subscription.delete()
            message = "Subscription removed"
        else:
            message = "Subscription added"

        return Response({"message": message})

    def get(self, request):
        user = request.user
        follow = Follow.objects.filter(user=user)
        serializer = FollowSerializer(follow, many=True)
        return Response(serializer.data)
