# Generated by Django 2.2.1 on 2020-09-07 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saleorderinvoicesApp', '0003_auto_20200907_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleorderinvoiceitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saleordersApp.SaleOrderItem'),
        ),
        migrations.DeleteModel(
            name='PublishedSaleOrderInvoice',
        ),
    ]