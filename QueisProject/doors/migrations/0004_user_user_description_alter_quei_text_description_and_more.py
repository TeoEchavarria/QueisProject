# Generated by Django 4.0.4 on 2022-04-30 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doors', '0003_remove_queicontent_autor_remove_queicontent_pub_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_description',
            field=models.CharField(default='Not description', max_length=120),
        ),
        migrations.AlterField(
            model_name='quei',
            name='text_description',
            field=models.CharField(default='Not description', max_length=120),
        ),
        migrations.AlterField(
            model_name='queicontent',
            name='text_content',
            field=models.TextField(default='Not text Content'),
        ),
    ]
