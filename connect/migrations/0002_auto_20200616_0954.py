# Generated by Django 3.0.6 on 2020-06-16 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='img',
            new_name='image',
        ),
    ]