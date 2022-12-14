# Generated by Django 3.2.16 on 2022-10-17 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20221017_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='bookings',
        ),
        migrations.AddField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.customer'),
        ),
        migrations.AddField(
            model_name='dessert',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.menu'),
        ),
        migrations.AddField(
            model_name='maindish',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.menu'),
        ),
        migrations.AddField(
            model_name='starter',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.menu'),
        ),
    ]
