# Generated by Django 4.2.10 on 2024-03-05 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_is_attending_attendance_is_attending_morning_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attendance',
        ),
    ]