# Generated by Django 2.2.1 on 2020-07-07 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='temp_field',
            field=models.CharField(default='temp', max_length=20),
            preserve_default=False,
        ),
    ]
