# Generated by Django 4.0.3 on 2022-05-07 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0010_agency_available_cars_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]