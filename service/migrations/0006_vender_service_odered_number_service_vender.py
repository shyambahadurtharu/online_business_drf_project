# Generated by Django 5.0.4 on 2024-04-26 03:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_service_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vender_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='odered_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='vender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.vender'),
        ),
    ]
