# Generated by Django 2.2.1 on 2020-10-19 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saleordersApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleorderitem',
            name='available_quantity',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=14),
        ),
        migrations.AddField(
            model_name='saleorderitem',
            name='billed_quantity',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=14),
        ),
    ]