# Generated by Django 4.2.7 on 2023-11-08 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythonapp', '0003_alter_userinfo_password_alter_userinfo_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]