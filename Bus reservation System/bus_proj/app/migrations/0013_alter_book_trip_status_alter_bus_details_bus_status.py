# Generated by Django 4.2.1 on 2023-06-08 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_book_trip_status_bus_details_bus_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='trip_status',
            field=models.CharField(default='yet to start', max_length=50),
        ),
        migrations.AlterField(
            model_name='bus_details',
            name='bus_status',
            field=models.CharField(default='Yet to start', max_length=20),
        ),
    ]
