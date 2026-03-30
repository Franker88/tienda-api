from django.urls import path
from rest_framework.routers import DefaultRouter

from products.views import ProductosView
from products.viewsets import ProductosViewSet

router = DefaultRouter()
router.register('', ProductosViewSet, basename='productos')

urlpatterns = [
    path('list/', ProductosView.as_view(), name='list_products')
] + router.urls
