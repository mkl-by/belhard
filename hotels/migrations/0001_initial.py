# Generated by Django 3.2.3 on 2021-06-03 11:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('avg_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('user', models.ManyToManyField(blank=True, related_name='rated_services', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, unique=True)),
                ('city', models.CharField(max_length=70)),
                ('star', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('works', models.BooleanField(default=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='imageshotel/%Y/%m/%d', verbose_name=' Изображение отеля')),
                ('manager', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_hotels', to=settings.AUTH_USER_MODEL)),
                ('rating', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotels.typeservice')),
            ],
        ),
        migrations.CreateModel(
            name='UserTypeService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveSmallIntegerField()),
                ('type_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rated_type_service', to='hotels.typeservice')),
                ('user', models.ForeignKey(default=3, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='rated_type_service', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'type_service')},
            },
        ),
    ]
