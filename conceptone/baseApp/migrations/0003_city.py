# Generated by Django 2.2.1 on 2020-07-08 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0002_province'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_code', models.CharField(max_length=16, unique=True)),
                ('city_name', models.CharField(max_length=256, unique=True)),
            ],
        ),
    ]
