# Generated by Django 2.2.1 on 2020-05-18 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salesApp', '0010_auto_20200518_1333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saleorder',
            old_name='total_amount',
            new_name='so_amount',
        ),
    ]
