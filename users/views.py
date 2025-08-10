from rest_framework.viewsets import ModelViewSet
from .models import Payments
from .serializers import PaymentsSerializers


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializers
    filterset_fields = ['course', 'lesson', 'payment_method']
    ordering_fields = ['date_pay']
