from rest_framework.routers import DefaultRouter

from pedidos.viewsets import DetallePedidosViewSet, PedidosViewSet

router = DefaultRouter()
router.register('', PedidosViewSet, basename='pedidos')
router.register('<int:id>', DetallePedidosViewSet, basename='detalle-pedidos')

urlpatterns = router.urls
