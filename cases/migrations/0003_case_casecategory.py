# Generated by Django 3.2.4 on 2021-08-06 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_mainbanner'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Название')),
                ('slug', models.CharField(blank=True, max_length=200, unique=True, verbose_name='slug (Не обязательно)')),
            ],
            options={
                'verbose_name': 'Название категории',
                'verbose_name_plural': 'Название категорий',
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название кейса')),
                ('img', models.ImageField(upload_to='media', verbose_name='Картинка')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.casecategory')),
            ],
            options={
                'verbose_name': 'Кейс',
                'verbose_name_plural': 'Кейсы',
            },
        ),
    ]
