# Generated by Django 4.1.13 on 2024-01-30 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_task_delete_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]