# Generated by Django 4.0.6 on 2022-10-17 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_remove_photos_id_photos_d_alter_photos_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photos',
            old_name='d',
            new_name='id',
        ),
    ]
