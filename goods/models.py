from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Nazwa')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Kategoria'
        verbose_name_plural ='Kategorie'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Nazwa')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Opis')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Obraz')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Cena')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Rabat w %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Ilość')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Kategoria')

    class Meta:
        db_table = 'product'
        verbose_name = 'Produkt'
        verbose_name_plural ='Produkty'

    def __str__(self):
        return f'{self.name} Ilość - {self.quantity}'

    def display_id(self):
        return f'{self.id:05}'

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)

        return self.price
