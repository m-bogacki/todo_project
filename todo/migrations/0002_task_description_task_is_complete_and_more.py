# Generated by Django 4.2.5 on 2024-01-21 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="description",
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="task",
            name="is_complete",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="task",
            name="due_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]