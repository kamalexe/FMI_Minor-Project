# Generated by Django 4.0.6 on 2022-09-26 17:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0007_farmersellproduct_likes_alter_tracker_updatedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='updateDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 26, 23, 22, 46, 289916)),
        ),
    ]
