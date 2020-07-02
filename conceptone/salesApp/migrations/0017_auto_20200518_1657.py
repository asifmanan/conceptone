# Generated by Django 2.2.1 on 2020-05-18 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salesApp', '0016_auto_20200518_1629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saleinvoiceitem',
            old_name='si_item_bill_quantity',
            new_name='bill_quantity',
        ),
        migrations.RenameField(
            model_name='saleinvoiceitem',
            old_name='si_number',
            new_name='sale_invoice',
        ),
        migrations.RenameField(
            model_name='saleinvoiceitem',
            old_name='si_item',
            new_name='sale_order_item',
        ),
        migrations.RenameField(
            model_name='saleinvoiceitem',
            old_name='si_item_tax_amount',
            new_name='tax_amount',
        ),
        migrations.RenameField(
            model_name='saleinvoiceitem',
            old_name='si_item_tax_rate',
            new_name='tax_rate',
        ),
        migrations.RenameField(
            model_name='saleinvoiceitem',
            old_name='si_item_total_amount',
            new_name='total_amount',
        ),
    ]
