# Generated by Django 4.2.3 on 2023-07-23 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_event_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='owner',
            field=models.IntegerField(default=1, verbose_name='Venue Owner'),
        ),
    ]
