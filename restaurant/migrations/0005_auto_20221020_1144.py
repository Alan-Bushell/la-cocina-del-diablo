# Generated by Django 3.2.16 on 2022-10-20 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_auto_20221020_1129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='lname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='pax',
            new_name='number_of_attendees',
        ),
    ]
