# Generated by Django 3.2.4 on 2021-08-06 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smm', '0007_metatags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariffs',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True, verbose_name='Цена'),
        ),
    ]
