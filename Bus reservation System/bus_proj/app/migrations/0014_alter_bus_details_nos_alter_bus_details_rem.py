# Generated by Django 4.2.1 on 2023-06-08 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_book_trip_status_alter_bus_details_bus_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus_details',
            name='nos',
            field=models.DecimalField(decimal_places=0, default=35, max_digits=2),
        ),
        migrations.AlterField(
            model_name='bus_details',
            name='rem',
            field=models.DecimalField(decimal_places=0, default=35, max_digits=2),
        ),
    ]
