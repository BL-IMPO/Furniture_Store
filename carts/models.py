from django.db import models

from users.models import User
from goods.models import Products


class CartQueryset(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)

        return 0


class Cart(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Użytkownik')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Produkt')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Ilość')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Data dodania')

    class Meta:
        db_table = 'cart'
        verbose_name = 'Koszyk'
        verbose_name_plural = 'Koszyk'

    objects = CartQueryset().as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        if self.user:
            return f"Koszyk {self.user.username} | Product {self.product.name} | Ilość {self.quantity}"

        return f" Anonymne koszyk  | Product {self.product.name} | Ilość {self.quantity}"
