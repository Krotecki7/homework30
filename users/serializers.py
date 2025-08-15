from rest_framework.serializers import ModelSerializer
from .models import Payments, User
from django.contrib.auth.hashers import make_password


class PaymentsSerializers(ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate_password(self, value: str) -> str:
        return make_password(value)
