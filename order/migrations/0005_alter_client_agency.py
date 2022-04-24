# Generated by Django 4.0.3 on 2022-04-23 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0008_alter_agency_user'),
        ('order', '0004_alter_order_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='agency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agency.agency'),
        ),
    ]