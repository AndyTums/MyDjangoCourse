from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ Модель: Пользователь """

    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    first_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Фамилия')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Телефон')
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name='Страна')
    photo = models.ImageField(upload_to='users/avatars/', blank=True, null=True, verbose_name='Фото')

    token = models.CharField(max_length=100, verbose_name='Token', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        permissions = [("can_block_user", "Блокировка пользователя")]

    def __str__(self):
        return self.email
