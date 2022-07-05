# Generated by Django 4.0.4 on 2022-05-08 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doors', '0010_comment_door'),
    ]

    operations = [
        migrations.AddField(
            model_name='door',
            name='text_content',
            field=models.TextField(default='Not text Content'),
        ),
        migrations.AddField(
            model_name='door',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='door',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='doors.door'),
        ),
        migrations.DeleteModel(
            name='DoorContent',
        ),
    ]