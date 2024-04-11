# Generated by Django 4.2.10 on 2024-04-02 10:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_alter_checkinout_check_in_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkinout',
            name='check_in_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='checkinout',
            name='check_out_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]