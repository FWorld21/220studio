# Generated by Django 3.2.4 on 2021-08-06 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0006_auto_20210806_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariffs',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Цена'),
        ),
    ]
