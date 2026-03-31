from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from products.models import Categorias, Productos
from products.serializers import CategoriasSerializer, ProductosSerializer

class ProductosView(ListAPIView):
    permission_classes = [IsAuthenticated]
    allowed_methods = ["GET"]
    serializer_class = ProductosSerializer
    queryset = Productos.objects.all()

class CategoriasView(ListAPIView):
    permission_classes = [IsAuthenticated]
    allowed_methods = ["GET"]
    serializer_class = CategoriasSerializer
    queryset = Categorias.objects.all()

