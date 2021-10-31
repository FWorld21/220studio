# Generated by Django 3.2.4 on 2021-07-26 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contextadv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContextAdvertisementTools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название инструмента')),
                ('img', models.ImageField(upload_to='media', verbose_name='Логотип инструмента')),
            ],
            options={
                'verbose_name': 'Инструмент контекстной рекламы',
                'verbose_name_plural': 'Инструменты контекстной рекламы',
            },
        ),
    ]