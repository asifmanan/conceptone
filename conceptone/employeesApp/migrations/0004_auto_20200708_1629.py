# Generated by Django 2.2.1 on 2020-07-08 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeesApp', '0003_auto_20200708_1527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='address_1',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='address_2',
        ),
    ]
