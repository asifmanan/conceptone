# Generated by Django 2.2.1 on 2020-06-23 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesApp', '0020_saleorderitem_so_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saleorderitem',
            name='so_amount',
        ),
        migrations.AddField(
            model_name='saleorder',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=14, verbose_name='Total Amount'),
        ),
    ]
