# Generated by Django 4.1.2 on 2023-06-27 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0041_remove_adminhod_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancereport',
            name='attendance',
        ),
        migrations.RemoveField(
            model_name='attendancereport',
            name='student_id',
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='AttendanceReport',
        ),
    ]
