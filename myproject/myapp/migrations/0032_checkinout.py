# Generated by Django 4.2.10 on 2024-04-02 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0031_delete_checkinout'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckInOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.IntegerField(default=205)),
                ('is_checked', models.BooleanField(default=True)),
                ('is_checked_out', models.BooleanField(default=False)),
                ('check_in_time', models.DateTimeField(blank=True, default=None, null=True)),
                ('check_out_time', models.DateTimeField(blank=True, default=None, null=True)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
