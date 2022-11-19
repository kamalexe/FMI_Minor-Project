# Generated by Django 4.0.6 on 2022-09-17 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmiapp', '0008_alter_usertype_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerinfo',
            name='usertype',
            field=models.CharField(default='farmer', max_length=20),
        ),
        migrations.AlterField(
            model_name='logininfo',
            name='usertype',
            field=models.CharField(default='admin', max_length=50),
        ),
        migrations.AlterField(
            model_name='merchantinfo',
            name='usertype',
            field=models.CharField(default='merchant', max_length=20),
        ),
        migrations.DeleteModel(
            name='UserType',
        ),
    ]