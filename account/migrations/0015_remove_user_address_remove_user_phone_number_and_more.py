# Generated by Django 4.2.5 on 2024-01-06 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0014_alter_address_latitude_alter_address_longitude"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="address",),
        migrations.RemoveField(model_name="user", name="phone_number",),
        migrations.RemoveField(model_name="user", name="role",),
        migrations.DeleteModel(name="Address",),
    ]
