# Generated by Django 3.2.4 on 2021-08-06 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brandbook', '0002_alter_worksteps_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariffs',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True, verbose_name='Цена'),
        ),
    ]
