# Generated by Django 2.2.1 on 2020-09-07 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saleorderinvoicesApp', '0005_publishedsaleorderinvoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishedsaleorderinvoice',
            name='invoice_number',
            field=models.CharField(max_length=56, null=True, unique=True),
        ),
    ]
