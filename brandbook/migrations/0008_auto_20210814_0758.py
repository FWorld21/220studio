# Generated by Django 3.2.4 on 2021-08-14 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brandbook', '0007_alter_worksteps_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='minibanner',
            old_name='img',
            new_name='desktop',
        ),
        migrations.RenameField(
            model_name='minibanner',
            old_name='mobile_img',
            new_name='mobile',
        ),
    ]
