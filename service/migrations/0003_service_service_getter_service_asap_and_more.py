# Generated by Django 5.0.4 on 2024-04-19 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_service_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='Service_getter',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='asap',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
