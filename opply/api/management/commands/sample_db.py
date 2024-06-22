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

        product1 = Product.objects.create(name='Cinnamon', price=2.99, stock=15)
        product2 = Product.objects.create(name='Paprika', price=3.75, stock=25)
        product3 = Product.objects.create(name='Turmeric', price=4.50, stock=10)
        product4 = Product.objects.create(name='Cumin', price=1.99, stock=20)
        product5 = Product.objects.create(name='Coriander', price=5.25, stock=30)
        product6 = Product.objects.create(name='Ginger', price=2.49, stock=18)
        product7 = Product.objects.create(name='Chili Powder', price=3.99, stock=22)
        product8 = Product.objects.create(name='Mustard Seeds', price=6.50, stock=12)
        product9 = Product.objects.create(name='Fenugreek', price=4.75, stock=8)
        product10 = Product.objects.create(name='Cardamom', price=7.99, stock=35)
        product11 = Product.objects.create(name='Nutmeg', price=8.25, stock=5)
        product12 = Product.objects.create(name='Cloves', price=6.49, stock=17)
        product13 = Product.objects.create(name='Bay Leaves', price=3.25, stock=40)
        product14 = Product.objects.create(name='Saffron', price=9.99, stock=3)
        product15 = Product.objects.create(name='Vanilla Beans', price=10.00, stock=7)

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
