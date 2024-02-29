# Generated by Django 2.2.1 on 2020-07-17 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standardinvoiceApp', '0003_auto_20200717_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardinvoiceitem',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
        migrations.AlterField(
            model_name='standardinvoiceitem',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
        migrations.AlterField(
            model_name='standardinvoiceitem',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
    ]
