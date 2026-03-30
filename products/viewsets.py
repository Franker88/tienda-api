from rest_framework.viewsets import ModelViewSet

from products.models import Productos
from products.serializers import ProductosSerializer
from rest_framework.permissions import IsAuthenticated

class ProductosViewSet(ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    authentication_classes = [IsAuthenticated]
    