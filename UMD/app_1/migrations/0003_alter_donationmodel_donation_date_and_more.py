# Generated by Django 4.0.1 on 2022-03-09 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0002_entry_alter_donationmodel_donation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationmodel',
            name='donation_date',
            field=models.DateField(default=datetime.datetime(2022, 3, 9, 17, 23, 40, 996652)),
        ),
        migrations.AlterField(
            model_name='donationmodel',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2022, 3, 9, 17, 23, 40, 996652)),
        ),
        migrations.AlterField(
            model_name='medicinestockmodel',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2022, 3, 9, 17, 23, 40, 996652)),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2022, 3, 9, 17, 23, 40, 996652)),
        ),
    ]