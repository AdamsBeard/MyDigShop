# Generated by Django 2.0.2 on 2018-02-12 06:42

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20180211_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_created=True, default=datetime.datetime.now)),
                ('email', models.EmailField(max_length=64, verbose_name='Email')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Ключ покупки')),
            ],
            options={
                'verbose_name_plural': 'Товары',
                'verbose_name': 'Товар',
            },
        ),
        migrations.AlterField(
            model_name='goods',
            name='datetime',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime.now),
        ),
    ]