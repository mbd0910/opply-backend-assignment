from django.contrib.auth.models import User
from rest_framework import serializers
from opply.api.models import Order, OrderProductQuantity, Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']


class ProductInventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['url', 'id', 'name', 'price', 'stock']
        extra_kwargs = {
            'url': {'view_name': 'product-detail', 'lookup_field': 'pk'}
        }


class OrderProductQuantitySerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderProductQuantity
        fields = ['product', 'quantity']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    product_quantities = OrderProductQuantitySerializer(many=True)

    class Meta:
        model = Order
        fields = ['user', 'order_date', 'product_quantities']


