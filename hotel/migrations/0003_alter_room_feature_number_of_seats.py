# Generated by Django 3.2.3 on 2021-05-21 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_alter_room_feature_number_of_seats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room_feature',
            name='number_of_seats',
            field=models.CharField(choices=[('1', 'одноместный'), ('2', 'двухместный'), ('3', 'трехместный'), ('L', 'Люкс')], max_length=1, unique=True),
        ),
    ]