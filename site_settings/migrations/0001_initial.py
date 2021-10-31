# Generated by Django 3.2.4 on 2021-08-04 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favicon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favicon', models.ImageField(upload_to='media', verbose_name='Favicon для сайта')),
            ],
            options={
                'verbose_name': 'Favicon',
                'verbose_name_plural': 'Favicon',
            },
        ),
        migrations.CreateModel(
            name='MetaTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400, verbose_name='Title')),
                ('keywords', models.TextField(verbose_name='Keywords (Через запятую)')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Мета тег',
                'verbose_name_plural': 'Мета теги',
            },
        ),
    ]