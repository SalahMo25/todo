# Generated by Django 5.0.6 on 2024-07-01 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='details',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='title',
        ),
    ]
