# Generated by Django 4.2.10 on 2024-04-09 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0052_alter_nightattendence_misno_alter_student_misno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nightattendence',
            name='room',
        ),
        migrations.RemoveField(
            model_name='nightattendence',
            name='student',
        ),
    ]
