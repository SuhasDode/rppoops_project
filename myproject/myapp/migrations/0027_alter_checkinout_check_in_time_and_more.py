# Generated by Django 4.2.10 on 2024-04-02 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_alter_checkinout_is_checked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkinout',
            name='check_in_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='checkinout',
            name='check_out_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
