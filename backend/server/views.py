from rest_framework import generics, permissions
from .models import BooleanValue, StringValue
from .serializers import BooleanValueSerializer, StringValueSerializer


class Boolean(generics.ListCreateAPIView):
    serializer_class = BooleanValueSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = BooleanValue.objects.all()


class String(generics.ListCreateAPIView):
    serializer_class = StringValueSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = StringValue.objects.all()
