# Generated by Django 4.0.3 on 2022-04-02 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agencyAdminstration', '0005_alter_vehicle_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='thumbnail',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='agencyAdminstration.vehicleimages'),
        ),
    ]
