# Generated by Django 3.2.23 on 2023-12-08 18:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_post_listing_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='listing_currency',
            field=models.IntegerField(choices=[('Pound Sterling', '£'), ('Dollar', '$'), ('Euro', '€'), ('Yen', '¥'), ('Won', '₩'), ('Lira', '₺'), ('Franc', '₣'), ('Rupee', '₹'), ('Dinar', 'د.ك')], default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='listing_timespan',
            field=models.IntegerField(choices=[('Per Week', 'p/w'), ('Per Month', 'p/m')], default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='listing_price',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^[0-9]')]),
        ),
    ]
