# Generated by Django 3.2.6 on 2021-08-09 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_rename_name_image_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image_url',
            new_name='name',
        ),
    ]