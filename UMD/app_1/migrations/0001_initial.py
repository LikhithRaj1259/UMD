# Generated by Django 4.0.1 on 2022-04-08 06:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DonationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default=0, max_length=20)),
                ('medicine_name', models.CharField(default='Medicine', max_length=100)),
                ('medicine_quantity', models.IntegerField(default=0)),
                ('donation_date', models.DateField(default=datetime.datetime(2022, 4, 8, 12, 11, 49, 958278))),
                ('expiry_date', models.DateField(default=datetime.datetime(2022, 4, 8, 12, 11, 49, 958278))),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('user_id', models.CharField(default='lr1', max_length=20)),
                ('name', models.CharField(default='lr', max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('adhaar', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('pass1', models.CharField(max_length=30)),
                ('image', models.ImageField(default='static/er_diagram.jpeg', upload_to='static')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default=0, max_length=20)),
                ('feedback', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MedicineStockModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(default='Medicine', max_length=100)),
                ('medicine_quantity', models.IntegerField(default=0)),
                ('expiry_date', models.DateField(default=datetime.datetime(2022, 4, 8, 12, 11, 49, 958278))),
            ],
        ),
        migrations.CreateModel(
            name='RequestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default=0, max_length=20)),
                ('medicine_name', models.CharField(default='Medicine', max_length=100)),
                ('medicine_quantity', models.IntegerField(default=0)),
                ('request_date', models.DateField(default=datetime.datetime(2022, 4, 8, 12, 11, 49, 958278))),
            ],
        ),
    ]
