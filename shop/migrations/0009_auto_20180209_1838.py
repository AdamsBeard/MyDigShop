# Generated by Django 2.0.2 on 2018-02-09 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20180209_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=256, verbose_name='ЧПУ URL'),
        ),
    ]