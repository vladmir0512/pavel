# Generated by Django 4.2.1 on 2023-06-01 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_client_options_alter_denyroom_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='photo',
        ),
    ]
