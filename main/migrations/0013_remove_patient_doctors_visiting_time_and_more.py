# Generated by Django 4.0 on 2022-05-08 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_message_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='doctors_visiting_time',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='symptoms',
        ),
    ]
