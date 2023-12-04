# Generated by Django 4.2.6 on 2023-11-28 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0014_order_costtopay'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_amount', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='CostToPay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.sales'),
        ),
    ]