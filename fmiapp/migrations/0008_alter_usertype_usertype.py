# Generated by Django 4.0.6 on 2022-09-17 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmiapp', '0007_usertype_alter_farmerinfo_usertype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertype',
            name='usertype',
            field=models.CharField(max_length=50),
        ),
    ]