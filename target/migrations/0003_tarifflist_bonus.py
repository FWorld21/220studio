# Generated by Django 3.2.4 on 2021-08-05 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0002_metatags'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarifflist',
            name='bonus',
            field=models.CharField(blank=True, max_length=400, verbose_name='Бонусы при приобретении этого тарифа'),
        ),
    ]