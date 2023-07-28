# Generated by Django 4.2.3 on 2023-07-28 19:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0012_event_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendance',
            field=models.ManyToManyField(blank=True, related_name='attend', to=settings.AUTH_USER_MODEL),
        ),
    ]