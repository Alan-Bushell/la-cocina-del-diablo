# Generated by Django 3.2.16 on 2022-10-06 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20221005_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.IntegerField(choices=[(0, 'Not Live'), (1, 'Live')], default=0),
        ),
    ]
