# Generated by Django 4.2.5 on 2023-11-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0008_remove_user_phone_number_user_phonenumber"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phoneNumber",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]