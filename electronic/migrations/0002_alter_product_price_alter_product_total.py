# Generated by Django 4.2.20 on 2025-04-19 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='total',
            field=models.DecimalField(decimal_places=5, default='', max_digits=10),
        ),
    ]
