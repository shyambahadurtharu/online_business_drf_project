# Generated by Django 5.0.4 on 2024-04-22 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas', '0002_rename_adress_gas_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gas',
            name='Service_getter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
