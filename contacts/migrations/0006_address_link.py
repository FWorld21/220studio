# Generated by Django 3.2.4 on 2021-07-24 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20210724_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='link',
            field=models.TextField(blank=True, verbose_name='Ссылка на локацию'),
        ),
    ]
