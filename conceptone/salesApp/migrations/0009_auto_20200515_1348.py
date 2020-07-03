# Generated by Django 2.2.1 on 2020-05-15 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salesApp', '0008_auto_20200501_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleinvoiceitem',
            name='si_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salesApp.SaleOrderItem', verbose_name='Item'),
        ),
        migrations.AlterField(
            model_name='saleinvoiceitem',
            name='si_item_tax_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=14, verbose_name='Tax Amount'),
        ),
        migrations.AlterField(
            model_name='saleinvoiceitem',
            name='si_item_total_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=14, verbose_name='Total Amount'),
        ),
        migrations.AlterField(
            model_name='saleinvoiceitem',
            name='si_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salesApp.SaleInvoice', verbose_name='Invoice Number'),
        ),
    ]