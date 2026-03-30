from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from products.models import Productos
from products.serializers import ProductosSerializer

class ProductosView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    allowed_methods = ["GET"]
    serializer_class = ProductosSerializer
    queryset = Productos.objects.all()

