# Generated by Django 4.0.3 on 2022-04-10 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationmodel',
            name='donation_date',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='donationmodel',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='medicinestockmodel',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 10, 15, 22, 8, 133160)),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='request_date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]