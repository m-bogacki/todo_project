# Generated by Django 4.2.5 on 2024-01-21 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0002_task_description_task_is_complete_and_more"),
    ]

    operations = [
        migrations.RenameField(model_name="task", old_name="name", new_name="title",),
    ]
