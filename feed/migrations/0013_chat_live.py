# Generated by Django 3.2.8 on 2021-12-20 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0012_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='live',
            field=models.URLField(blank=True),
        ),
    ]
