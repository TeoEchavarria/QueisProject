# Generated by Django 4.0.4 on 2022-05-14 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doors', '0013_remove_user_wallet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quei',
            name='door',
        ),
    ]
