# Generated by Django 4.1.2 on 2023-05-07 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0016_alter_subjects_subject_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]