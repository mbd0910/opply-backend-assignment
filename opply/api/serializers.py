from django.contrib.auth.models import Group, User
from rest_framework import serializers
from opply.api.models import Order, OrderProductQuantity, Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price']


class OrderProductQuantitySerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderProductQuantity
        fields = ['product', 'quantity']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    order_product_quantity = OrderProductQuantitySerializer()

    class Meta:
        model = Order
        fields = ['order_date', 'order_product_quantity']


