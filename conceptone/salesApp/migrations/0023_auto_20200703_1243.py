# Generated by Django 2.2.1 on 2020-07-03 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salesApp', '0022_auto_20200702_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleorderitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='itemsApp.Item', verbose_name='Item'),
        ),
    ]