# Generated by Django 2.0.2 on 2018-02-09 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20180209_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(max_length=32),
        ),
    ]
