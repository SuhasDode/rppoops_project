# Generated by Django 4.2.10 on 2024-04-01 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0017_delete_admin_remove_attendance_user_delete_feature_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=100)),
                ('room', models.IntegerField(default=205)),
            ],
        ),
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('date_of_leave', models.CharField(default='1-1-2024', max_length=20)),
                ('is_attending_morning', models.BooleanField(default=True)),
                ('is_attending_night', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]