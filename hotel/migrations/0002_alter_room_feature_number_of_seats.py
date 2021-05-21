# Generated by Django 3.2.3 on 2021-05-20 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room_feature',
            name='number_of_seats',
            field=models.CharField(choices=[('1', 'одноместный'), ('2', 'двухместный'), ('3', 'трехместный'), ('L', 'Люкс')], max_length=1),
        ),
    ]