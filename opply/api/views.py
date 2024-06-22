from opply.api.models import Product, Order
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from opply.api.serializers import ProductInventorySerializer, OrderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductInventorySerializer
    permission_classes = [IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product_quantities = serializer.validated_data['product_quantities']
        # Only accept an order if the requested quantity of every product is in stock
        for product_quantity in product_quantities:
            product = product_quantity['product']
            quantity = product_quantity['quantity']
            if quantity > product.stock:
                return Response({'error': f"Only {product.stock} units of {product.name} available."},
                                status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

