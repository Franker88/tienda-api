from django.contrib.auth.models import User

from rest_framework import mixins, viewsets, status, response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from .serializers import RegisterUserSerializer

class RegisterUserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAdminUser]

    def create(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return response.Response(RegisterUserSerializer(user).data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)