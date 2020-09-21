# Generated by Django 2.2.1 on 2020-09-08 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saleorderinvoicesApp', '0009_auto_20200908_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishedsaleorderinvoice',
            name='invoice',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='published_invoice', to='saleorderinvoicesApp.SaleOrderInvoice'),
        ),
        migrations.AlterField(
            model_name='saleorderinvoiceitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='saleordersApp.SaleOrderItem'),
        ),
    ]