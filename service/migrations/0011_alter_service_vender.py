# Generated by Django 5.0.4 on 2024-04-28 05:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_rename_odered_number_service_service_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='vender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.vender'),
        ),
    ]