# Generated by Django 4.2.10 on 2024-04-05 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0043_notice_alter_attendance_date_of_leave_laundrybooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='is_penalty',
            field=models.BooleanField(default=False),
        ),
    ]
