from django.db import models

from users.models import User
from goods.models import Products


class OrderItemQueryset(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name="Uzistkownik", default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Data utworzenia zamówienia")
    phone_number = models.CharField(max_length=20, verbose_name="Numer telefonu")
    requires_delivery = models.BooleanField(default=False, verbose_name="Wymagana dostawa")
    delivery_address = models.TextField(null=True, blank=True, verbose_name="Adres dostawy")
    payment_on_get = models.BooleanField(default=False, verbose_name="Metoda płatności")
    is_paid = models.BooleanField(default=False, verbose_name="Płatny")
    status = models.CharField(max_length=50, default="In process", verbose_name="Status zamówienia")

    class Meta:
        db_table = "order"
        verbose_name = "Zamówienie"
        verbose_name_plural = 'Zamówieny'
        ordering = ("id",)

    def __str__(self):
        return f"Zamówienie № {self.pk} | Kupujący {self.user.first_name} {self.user.last_name} "


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, on_delete=models.SET_DEFAULT, null=True, verbose_name="Produkty", default=None)
    name = models.CharField(max_length=150, verbose_name="Imie")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Cena")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Ilość")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Data utworzenia zamówienia")

    class Meta:
        db_table = "order_item"
        verbose_name = "Sprzedane towary"
        verbose_name_plural = "Sprzedane towary"
        ordering = ("id",)
    def products_price(self):
        return round(self.price * self.quantity, 2)

    def __str__(self):
        return f"Zamówienie № {self.order.pk} | Product {self.name}"

