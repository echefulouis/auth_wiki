# Generated by Django 3.2.3 on 2022-07-25 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_rename_libray_name_post_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='library_body',
            new_name='library_cotent',
        ),
    ]