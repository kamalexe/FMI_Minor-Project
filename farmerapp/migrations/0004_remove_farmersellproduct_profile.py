# Generated by Django 4.0.6 on 2022-09-17 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0003_alter_profile_farmername'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmersellproduct',
            name='profile',
        ),
    ]