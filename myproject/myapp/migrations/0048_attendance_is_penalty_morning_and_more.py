# Generated by Django 4.2.10 on 2024-04-07 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0047_attendance_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='is_penalty_morning',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attendance',
            name='is_penalty_night',
            field=models.BooleanField(default=False),
        ),
    ]
