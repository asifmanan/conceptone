# Generated by Django 2.2.1 on 2020-06-19 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudbasic', '0002_auto_20200612_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxrate',
            name='tax_jurisdiction',
            field=models.CharField(default='Federal', max_length=64),
        ),
    ]