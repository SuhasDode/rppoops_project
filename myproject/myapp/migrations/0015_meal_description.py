# Generated by Django 4.2.10 on 2024-04-01 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='description',
            field=models.CharField(default='bcd', max_length=100),
        ),
    ]
