# Generated by Django 4.2.10 on 2024-03-06 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_attendance_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='date_of_leave',
            field=models.CharField(default='1-1-2024', max_length=20),
        ),
    ]