# Generated by Django 4.1.1 on 2022-09-23 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='logged_on',
        ),
    ]
