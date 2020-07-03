# Generated by Django 2.2.1 on 2020-07-02 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crudbasic', '0006_delete_company'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Suppliers',
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customersApp.Customer'),
        ),
        migrations.DeleteModel(
            name='Customers',
        ),
    ]