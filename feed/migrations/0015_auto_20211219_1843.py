# Generated by Django 3.2.8 on 2021-12-20 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0014_alter_chat_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Live',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.URLField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='chat',
            name='live',
        ),
    ]
