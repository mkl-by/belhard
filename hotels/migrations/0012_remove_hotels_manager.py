# Generated by Django 3.2.3 on 2021-06-28 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0011_alter_hotels_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotels',
            name='manager',
        ),
    ]
