# Generated by Django 4.0.1 on 2022-01-12 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sex',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]