# Generated by Django 3.2.2 on 2021-05-19 09:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='date_sold',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='items',
            name='site_own',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='feedback',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='imgscr',
            field=models.URLField(blank=True),
        ),
    ]
