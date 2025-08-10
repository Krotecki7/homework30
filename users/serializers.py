from rest_framework.serializers import ModelSerializer
from .models import Payments


class PaymentsSerializers(ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"
