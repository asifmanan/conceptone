# Generated by Django 2.2.1 on 2020-04-24 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_code', models.CharField(max_length=16, unique=True)),
                ('company_name', models.CharField(max_length=128)),
                ('company_address', models.CharField(max_length=264)),
                ('company_ntn_number', models.CharField(max_length=128)),
                ('company_city', models.CharField(max_length=128)),
                ('company_phone', models.CharField(max_length=128)),
                ('company_fax', models.CharField(blank=True, max_length=128)),
                ('company_email', models.EmailField(max_length=192)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_code', models.CharField(max_length=16, unique=True)),
                ('customer_name', models.CharField(max_length=128, unique=True)),
                ('customer_address', models.CharField(max_length=264)),
                ('customer_city', models.CharField(max_length=128)),
                ('customer_phone', models.CharField(blank=True, max_length=128)),
                ('customer_fax', models.CharField(blank=True, max_length=128)),
                ('customer_email', models.EmailField(blank=True, max_length=192)),
                ('customer_ntn_number', models.CharField(blank=True, max_length=128)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.CharField(max_length=16, unique=True)),
                ('item_description', models.CharField(max_length=192)),
                ('item_uom', models.CharField(max_length=16)),
                ('item_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=14)),
                ('item_type', models.CharField(choices=[('Goods', 'Goods'), ('Services', 'Services')], max_length=8)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_code', models.CharField(max_length=16, unique=True)),
                ('supplier_name', models.CharField(max_length=128, unique=True)),
                ('supplier_address', models.CharField(max_length=264)),
                ('supplier_city', models.CharField(max_length=128)),
                ('supplier_phone', models.CharField(blank=True, max_length=128)),
                ('supplier_fax', models.CharField(blank=True, max_length=128)),
                ('supplier_email', models.EmailField(blank=True, max_length=192)),
                ('supplier_ntn_number', models.CharField(blank=True, max_length=128)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaxRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_code', models.CharField(max_length=16)),
                ('tax_name', models.CharField(max_length=64)),
                ('tax_value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.CharField(max_length=16)),
                ('po_date', models.DateField()),
                ('po_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=14)),
                ('po_tax_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=14)),
                ('po_draft', models.BooleanField(default=True)),
                ('po_publish', models.BooleanField(default=False)),
                ('po_publish_date', models.DateTimeField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('po_supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudbasic.Suppliers')),
                ('po_tax', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crudbasic.TaxRate')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_code', models.CharField(max_length=16, unique=True)),
                ('project_name', models.CharField(max_length=128, unique=True)),
                ('project_city', models.CharField(max_length=128)),
                ('project_status', models.CharField(choices=[('Prospective', 'Prospective'), ('Completed', 'Completed'), ('On-Going', 'On-Going')], max_length=16)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('project_customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crudbasic.Customers')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_line_number', models.IntegerField(verbose_name='Line')),
                ('order_quantity', models.DecimalField(decimal_places=2, max_digits=14, verbose_name='Quantity')),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=14, verbose_name='Purchase Price')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=14)),
                ('variation_number', models.IntegerField(default=0)),
                ('variation_quantity', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crudbasic.Items', verbose_name='Item')),
                ('po_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudbasic.PurchaseOrder')),
            ],
        ),
    ]