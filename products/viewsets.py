from rest_framework.viewsets import ModelViewSet

from products.models import Categorias, Productos
from products.serializers import CategoriasSerializer, ProductosSerializer
from rest_framework.permissions import IsAuthenticated

class ProductosViewSet(ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    permission_classes = [IsAuthenticated]
    
class CategoriasViewSet(ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer
    permission_classes = [IsAuthenticated]