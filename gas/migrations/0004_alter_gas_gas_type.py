# Generated by Django 5.0.4 on 2024-04-22 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas', '0003_alter_gas_service_getter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gas',
            name='gas_type',
            field=models.CharField(max_length=100),
        ),
    ]
