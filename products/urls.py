from django.urls import path
from rest_framework.routers import DefaultRouter

from products.views import ProductosView
from products.viewsets import CategoriasViewSet, ProductosViewSet

router = DefaultRouter()
router.register('categories', CategoriasViewSet, basename='categories')
router.register('', ProductosViewSet, basename='products')

urlpatterns = [
    path('list/', ProductosView.as_view(), name='list_products')
] + router.urls
