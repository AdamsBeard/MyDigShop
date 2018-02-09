from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=32)
    desc = models.TextField(verbose_name='Описание', max_length=10000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

class Category(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=32)
    desc = models.TextField(verbose_name='Описание', max_length=10000)
    slug = models.SlugField(verbose_name='ЧПУ URL', max_length=256)
    visible = models.BooleanField(verbose_name='Показать', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'