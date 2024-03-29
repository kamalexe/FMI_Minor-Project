# Generated by Django 4.0.6 on 2022-09-18 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=100)),
                ('customer', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=150)),
                ('panno', models.CharField(default='', max_length=10)),
                ('gstno', models.CharField(default='', max_length=15)),
                ('product', models.CharField(default='', max_length=150)),
                ('qty', models.CharField(default='', max_length=10)),
                ('price', models.CharField(default='', max_length=12)),
                ('city', models.CharField(default='', max_length=30)),
                ('state', models.CharField(default='', max_length=30)),
                ('zip', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
