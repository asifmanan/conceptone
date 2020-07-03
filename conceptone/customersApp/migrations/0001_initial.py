# Generated by Django 2.2.1 on 2020-06-26 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
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
    ]