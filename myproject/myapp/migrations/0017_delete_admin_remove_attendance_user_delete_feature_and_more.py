# Generated by Django 4.2.10 on 2024-04-01 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_alter_meal_day_of_week'),
    ]

    operations = [
        migrations.DeleteModel(
            name='admin',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='user',
        ),
        migrations.DeleteModel(
            name='feature',
        ),
        migrations.DeleteModel(
            name='attendance',
        ),
    ]
