# Generated by Django 4.0.6 on 2022-10-20 13:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0052_alter_tracker_updatedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='updateDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 20, 19, 8, 39, 261378)),
        ),
    ]
