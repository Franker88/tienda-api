from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


from .serializers import PedidosSerializer, DetallePedidosSerializer
from .models import Pedidos, DetallePedidos

class PedidosViewSet(viewsets.ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer

class DetallePedidosViewSet(viewsets.ModelViewSet):
    queryset = DetallePedidos.objects.all()
    serializer_class = DetallePedidosSerializer