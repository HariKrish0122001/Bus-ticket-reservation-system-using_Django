# Generated by Django 4.2.1 on 2023-05-25 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_user_details_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]