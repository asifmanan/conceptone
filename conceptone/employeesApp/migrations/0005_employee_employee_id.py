# Generated by Django 2.2.1 on 2020-07-08 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeesApp', '0004_auto_20200708_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='employee_id',
            field=models.CharField(default='', max_length=16),
            preserve_default=False,
        ),
    ]