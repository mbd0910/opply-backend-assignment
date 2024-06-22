from django.contrib.auth.models import User
from rest_framework import serializers
from opply.api.models import Order, OrderProductQuantity, Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    Basic product serializer without stock count - used when we want to return the products in an order without
    including current stock levels.
    """
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']


class ProductInventorySerializer(serializers.HyperlinkedModelSerializer):
    """
    Separate serializer when browsing the product inventory as we want to return how many products are in stock.
    """
    class Meta:
        model = Product
        fields = ['url', 'id', 'name', 'price', 'stock']
        extra_kwargs = {
            'url': {'view_name': 'product-detail', 'lookup_field': 'pk'}
        }


class OrderProductQuantitySerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer(read_only=True)
    # For writes (POST requests), only require the product ID
    product_id = serializers.PrimaryKeyRelatedField(source='product', queryset=Product.objects.all(), write_only=True)

    class Meta:
        model = OrderProductQuantity
        fields = ['product', 'product_id', 'quantity']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    # For writes (POST requests), only require the user ID
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all(), write_only=True)
    product_quantities = OrderProductQuantitySerializer(many=True)

    class Meta:
        model = Order
        fields = ['user', 'user_id', 'order_date', 'product_quantities']

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
