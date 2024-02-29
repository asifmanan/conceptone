# Generated by Django 2.2.1 on 2020-06-26 10:29

from django.db import migrations, models


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
    ]
