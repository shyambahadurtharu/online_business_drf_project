# Generated by Django 5.0.4 on 2024-04-26 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas', '0010_alter_gas_odered_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gas',
            name='odered_number',
            field=models.CharField(default='sdfgh', editable=False, max_length=100),
        ),
    ]
