# Generated by Django 4.2.7 on 2023-11-19 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankoffer',
            name='dangerous_indicator',
            field=models.BooleanField(default=False),
        ),
    ]
