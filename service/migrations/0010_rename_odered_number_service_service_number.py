# Generated by Django 5.0.4 on 2024-04-28 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_alter_service_odered_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='odered_number',
            new_name='service_number',
        ),
    ]
