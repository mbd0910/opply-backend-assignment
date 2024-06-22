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
    user = serializers.SerializerMethodField()
    product_quantities = OrderProductQuantitySerializer(many=True)

    class Meta:
        model = Order
        fields = ['user', 'order_date', 'product_quantities']

    def create(self, validated_data):
        product_quantities_data = validated_data.pop('product_quantities')
        order = Order.objects.create(**validated_data)
        for product_quantity in product_quantities_data:
            OrderProductQuantity.objects.create(order=order, **product_quantity)
            product = product_quantity['product']
            quantity = product_quantity['quantity']
            product.stock -= quantity
            product.save()
        return order

    def get_user(self, obj):
        if self.context.get('request').method == 'GET':
            return UserSerializer(obj.user).data
        # Use PrimaryKeyRelatedField for POST requests so we only have to provide an ID
        return obj.user.id

