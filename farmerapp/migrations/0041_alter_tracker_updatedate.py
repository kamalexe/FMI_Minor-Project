# Generated by Django 4.0.6 on 2022-10-19 09:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0040_alter_tracker_updatedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='updateDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 19, 14, 52, 7, 522004)),
        ),
    ]
