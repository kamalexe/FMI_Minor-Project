# Generated by Django 4.0.6 on 2022-09-20 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0005_tracker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='orderId',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='orderStatus',
            field=models.CharField(default='Your Order has been placed', max_length=100),
        ),
    ]
