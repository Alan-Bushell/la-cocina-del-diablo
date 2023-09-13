# Generated by Django 3.2.16 on 2023-09-13 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0015_remove_booking_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='last_name',
        ),
        migrations.AddField(
            model_name='booking',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
