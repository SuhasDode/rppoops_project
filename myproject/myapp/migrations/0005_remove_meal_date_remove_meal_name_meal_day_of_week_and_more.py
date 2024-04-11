# Generated by Django 4.2.10 on 2024-03-04 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_meal_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='date',
        ),
        migrations.RemoveField(
            model_name='meal',
            name='name',
        ),
        migrations.AddField(
            model_name='meal',
            name='day_of_week',
            field=models.IntegerField(default=6, verbose_name=10),
        ),
        migrations.AddField(
            model_name='meal',
            name='meal_name',
            field=models.CharField(default='abc', max_length=100),
        ),
    ]