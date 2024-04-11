# Generated by Django 4.2.10 on 2024-04-02 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_checkinout_student_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkinout',
            name='is_checked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checkinout',
            name='is_checked_out',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='checkinout',
            name='check_in_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
