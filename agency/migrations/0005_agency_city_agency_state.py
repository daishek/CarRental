# Generated by Django 4.0.3 on 2022-04-17 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0004_alter_agency_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='agency',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
