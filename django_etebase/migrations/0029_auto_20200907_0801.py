# Generated by Django 3.1 on 2020-09-07 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("django_etebase", "0028_auto_20200907_0754"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="collectioninvitation",
            name="accessLevelOld",
        ),
        migrations.RemoveField(
            model_name="collectionmember",
            name="accessLevelOld",
        ),
    ]
