# Generated by Django 5.0 on 2023-12-27 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0004_cart_unit_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
