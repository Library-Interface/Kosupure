# Generated by Django 3.2.8 on 2021-12-15 21:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0009_events_attending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='attending',
            field=models.ManyToManyField(blank=True, related_name='attending_events', to=settings.AUTH_USER_MODEL),
        ),
    ]
