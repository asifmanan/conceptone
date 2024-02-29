# Generated by Django 2.2.1 on 2020-07-22 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('baseApp', '0004_department'),
        ('customersApp', '0001_initial'),
        ('taxesApp', '0002_auto_20200706_1705'),
        ('projectsApp', '0003_remove_project_temp_field'),
        ('itemsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('so_number', models.CharField(max_length=56)),
                ('so_date', models.DateField()),
                ('buyer_po_number', models.CharField(max_length=56)),
                ('buyer_po_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=14)),
                ('tax_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=14)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=14)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customersApp.Customer')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projectsApp.Project')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='baseApp.Company')),
            ],
        ),
        migrations.CreateModel(
            name='SaleOrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_number', models.IntegerField()),
                ('order_quantity', models.DecimalField(decimal_places=2, max_digits=14)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=14)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=14)),
                ('tax_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=14)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=14)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='itemsApp.Item')),
                ('sale_order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='saleordersApp.SaleOrder')),
                ('tax', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='taxesApp.Tax')),
            ],
        ),
    ]
