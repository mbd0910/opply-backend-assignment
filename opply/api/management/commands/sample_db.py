from django.core.management.base import BaseCommand
from opply.api.models import Product, Order, OrderProductQuantity, User


class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **kwargs):
        OrderProductQuantity.objects.all().delete()
        Order.objects.all().delete()
        Product.objects.all().delete()
        User.objects.all().delete()

        user1 = User.objects.create_user(username='austin.payne', email='austin.payne@testdata.com', password='pw1')
        user2 = User.objects.create_user(username='jasmine.mathis', email='jasmine.mathis@testdata.com', password='pw2')

        product1 = Product.objects.create(name='Sugar', price=1.23, stock=5)
        product2 = Product.objects.create(name='Coriander', price=4, stock=0)
        product3 = Product.objects.create(name='Flour', price=13, stock=1)
        product4 = Product.objects.create(name='Salt', price=18, stock=2)

        order1 = Order.objects.create(user=user1)
        order2 = Order.objects.create(user=user2)
        order3 = Order.objects.create(user=user1)
        order4 = Order.objects.create(user=user1)

        OrderProductQuantity.objects.create(order=order1, product=product1, quantity=1)
        OrderProductQuantity.objects.create(order=order1, product=product2, quantity=2)
        OrderProductQuantity.objects.create(order=order1, product=product3, quantity=3)
        OrderProductQuantity.objects.create(order=order1, product=product4, quantity=4)

        OrderProductQuantity.objects.create(order=order2, product=product1, quantity=5)
        OrderProductQuantity.objects.create(order=order2, product=product2, quantity=5)
        OrderProductQuantity.objects.create(order=order2, product=product4, quantity=5)

        OrderProductQuantity.objects.create(order=order3, product=product2, quantity=2)
        OrderProductQuantity.objects.create(order=order3, product=product3, quantity=1)

        OrderProductQuantity.objects.create(order=order4, product=product1, quantity=100)
