# Generated by Django 4.2.1 on 2023-05-18 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='seat_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
