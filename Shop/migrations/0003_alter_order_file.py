# Generated by Django 4.2.6 on 2023-11-08 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_alter_order_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='file',
            field=models.FileField(upload_to='print_files/$<django.db.models.fields.CharField>'),
        ),
    ]