# Generated by Django 4.1.1 on 2022-09-24 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_login_logged_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='applied_on',
            field=models.DateField(auto_now=True),
        ),
    ]
