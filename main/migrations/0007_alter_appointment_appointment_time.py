# Generated by Django 4.0 on 2022-04-30 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_appointment_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_time',
            field=models.DateTimeField(null=True),
        ),
    ]