# Generated by Django 3.2.23 on 2023-12-08 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='listing_price',
            field=models.IntegerField(choices=[('Per Week', 'p/w'), ('Per Month', 'p/m')], default=0),
        ),
    ]
