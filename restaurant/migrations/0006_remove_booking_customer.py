# Generated by Django 3.2.16 on 2022-10-21 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_auto_20221020_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='customer',
        ),
    ]
