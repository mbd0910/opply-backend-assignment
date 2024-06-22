from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(0.01)])
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'


class Order(models.Model):
    user = models.ForeignKey(User, models.RESTRICT)
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'orders'


class OrderProductQuantity(models.Model):
    order = models.ForeignKey(Order, models.RESTRICT, related_name='product_quantities')
    product = models.ForeignKey(Product, models.RESTRICT)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        db_table = 'order_product_quantities'
        constraints = [
            models.UniqueConstraint(fields=['order', 'product'], name='unique_order_product')
        ]
