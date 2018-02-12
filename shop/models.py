from django.db import models
from django.utils.timezone import datetime
import uuid

# Create your models here.
class Notice(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=32)
    desc = models.TextField(verbose_name='Описание', max_length=10000)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=32)
    desc = models.TextField(verbose_name='Описание', max_length=10000)
    slug = models.SlugField(verbose_name='ЧПУ URL', max_length=256)
    price = models.FloatField(verbose_name='Цена', default=0, blank=False)
    visible = models.BooleanField(verbose_name='Показать', default=True)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Goods(models.Model):
    fkey = models.ForeignKey(Category, verbose_name='Категория товара', on_delete=False)
    good = models.CharField(verbose_name='Товар', max_length=32)
    desc = models.TextField(verbose_name='Описание', max_length=10000)
    datetime = models.DateTimeField(auto_created=True, default=datetime.now)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.good


class Buy(models.Model):
    email = models.EmailField(verbose_name='Email', max_length=64)
    datetime = models.DateTimeField(auto_created=True, default=datetime.now)
    uid = models.UUIDField(verbose_name='Ключ покупки', default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.email