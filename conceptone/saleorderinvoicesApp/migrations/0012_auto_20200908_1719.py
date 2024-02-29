# Generated by Django 2.2.1 on 2020-09-08 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saleorderinvoicesApp', '0011_auto_20200908_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleorderinvoiceitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='saleordersApp.SaleOrderItem'),
        ),
        migrations.AlterField(
            model_name='saleorderinvoiceitem',
            name='sale_order_invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saleorderinvoicesApp.SaleOrderInvoice'),
        ),
    ]
