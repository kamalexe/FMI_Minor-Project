# Generated by Django 4.0.6 on 2022-09-27 17:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0017_alter_tracker_updatedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='updateDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 27, 22, 46, 36, 813179)),
        ),
    ]
