# Generated by Django 4.2.10 on 2024-04-02 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_alter_checkinout_check_in_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkinout',
            name='student_name',
        ),
        migrations.AlterField(
            model_name='checkinout',
            name='check_in_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='checkinout',
            name='check_out_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
