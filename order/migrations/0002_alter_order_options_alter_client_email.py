# Generated by Django 4.0.3 on 2022-04-23 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
