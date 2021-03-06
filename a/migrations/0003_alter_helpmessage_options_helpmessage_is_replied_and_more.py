# Generated by Django 4.0.3 on 2022-05-23 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a', '0002_alter_helpmessage_date_added'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='helpmessage',
            options={'ordering': ['-date_added']},
        ),
        migrations.AddField(
            model_name='helpmessage',
            name='is_replied',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='helpmessage',
            name='reply',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='helpmessage',
            name='reply_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
