# Generated by Django 4.0.1 on 2022-01-07 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
