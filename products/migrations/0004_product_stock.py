# Generated by Django 5.1 on 2024-08-17 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_products_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
