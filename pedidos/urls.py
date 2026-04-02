from rest_framework.routers import DefaultRouter

from pedidos.viewsets import DetallePedidosViewSet, PedidosViewSet

router = DefaultRouter()
router.register('<int:id>', DetallePedidosViewSet, basename='detalle-pedidos')
router.register('', PedidosViewSet, basename='pedidos')

urlpatterns = router.urls
