# Generated by Django 4.2.6 on 2023-11-04 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_stud_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stud_history',
            name='ended',
        ),
        migrations.RemoveField(
            model_name='stud_history',
            name='started',
        ),
        migrations.RemoveField(
            model_name='teach_history',
            name='length',
        ),
        migrations.RemoveField(
            model_name='teach_history',
            name='started',
        ),
    ]
