# Generated by Django 3.2.4 on 2021-07-23 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cooperate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cooperate_title', models.CharField(max_length=300, verbose_name='Название компании')),
                ('cooperate_img', models.ImageField(upload_to='media', verbose_name='Лого компании')),
            ],
            options={
                'verbose_name': 'Тариф',
                'verbose_name_plural': 'Тарифы',
            },
        ),
        migrations.CreateModel(
            name='MainBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_banner_title', models.CharField(max_length=200, verbose_name='Заголовок главного баннера для SMM')),
                ('main_banner_subtitle', models.CharField(blank=True, max_length=200, verbose_name='Подзаголовок главного баннера для SMM')),
                ('main_banner_logo', models.ImageField(blank=True, upload_to='media', verbose_name='Картинка баннера для SMM')),
            ],
            options={
                'verbose_name': 'Главный баннер для SMM',
                'verbose_name_plural': 'Главные баннеры для SMM',
            },
        ),
        migrations.CreateModel(
            name='MiniBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mini_banner_img', models.ImageField(blank=True, upload_to='media', verbose_name='Картинка мини-баннера для SMM')),
            ],
            options={
                'verbose_name': 'Мини-баннер для SMM',
                'verbose_name_plural': 'Мини-баннеры для SMM',
            },
        ),
        migrations.CreateModel(
            name='Tariffs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tariff_title', models.CharField(max_length=250, verbose_name='Название тарифа')),
                ('tariff_price', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Цена тарифа')),
            ],
            options={
                'verbose_name': 'Тариф',
                'verbose_name_plural': 'Тарифы',
            },
        ),
        migrations.CreateModel(
            name='TariffList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tariff_list', models.CharField(max_length=250, verbose_name='Что в себя включает?')),
                ('tariff', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='smm.tariffs', verbose_name='Для тарифа')),
            ],
            options={
                'verbose_name': 'Список услуг',
                'verbose_name_plural': 'Список услуг',
            },
        ),
    ]
