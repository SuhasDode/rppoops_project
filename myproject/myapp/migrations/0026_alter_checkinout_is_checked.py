# Generated by Django 4.2.10 on 2024-04-02 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_alter_checkinout_check_in_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkinout',
            name='is_checked',
            field=models.BooleanField(default=True),
        ),
    ]
