# Generated by Django 4.2.3 on 2023-07-12 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_host'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='host',
            field=models.CharField(max_length=30),
        ),
    ]
