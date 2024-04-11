# Generated by Django 4.2.10 on 2024-03-03 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_room_guest_checkinout'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='checkinout',
            name='guest',
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
        migrations.AddField(
            model_name='checkinout',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.student'),
        ),
    ]
