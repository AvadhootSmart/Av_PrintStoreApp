# Generated by Django 4.2.6 on 2023-11-28 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0013_blackandwhiteprice_colorprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='CostToPay',
            field=models.IntegerField(default=0),
        ),
    ]