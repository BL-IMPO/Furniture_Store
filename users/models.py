from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name="Awatar")

    class Meta:
        db_table = 'user'
        verbose_name = 'Użytkownica'
        verbose_name_plural = 'Użytkownicy'

    def __str__(self):
        return self.username