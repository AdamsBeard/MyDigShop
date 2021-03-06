# Generated by Django 2.0.2 on 2018-02-11 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_category_visible'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_created=True)),
                ('good', models.CharField(max_length=32, verbose_name='Товар')),
                ('desc', models.TextField(max_length=10000, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='price',
            field=models.FloatField(default=0, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='goods',
            name='fkey',
            field=models.ForeignKey(on_delete=False, to='shop.Category', verbose_name='Категория товара'),
        ),
    ]
