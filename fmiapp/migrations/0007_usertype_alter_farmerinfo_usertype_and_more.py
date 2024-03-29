# Generated by Django 4.0.6 on 2022-09-17 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fmiapp', '0006_farmerinfo_password_farmerinfo_userid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertype', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='farmerinfo',
            name='usertype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fmiapp.usertype'),
        ),
        migrations.AlterField(
            model_name='merchantinfo',
            name='usertype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fmiapp.usertype'),
        ),
    ]
