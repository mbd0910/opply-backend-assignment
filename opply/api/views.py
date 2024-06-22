from django.contrib.auth.models import Group, User
from opply.api.models import Product, Order
from rest_framework import permissions, viewsets

from opply.api.serializers import ProductInventorySerializer, OrderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductInventorySerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


