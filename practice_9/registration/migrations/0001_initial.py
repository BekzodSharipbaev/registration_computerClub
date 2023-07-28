# Generated by Django 4.2.2 on 2023-07-27 14:30

import django.core.validators
from django.db import migrations, models
import registration.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('username', models.CharField(max_length=200, validators=[registration.validators.validate_username], verbose_name='username')),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='email')),
                ('password', models.CharField(max_length=100, validators=[registration.validators.validate_password, registration.validators.validate_positive_number], verbose_name='password')),
                ('phone_number', models.PositiveSmallIntegerField(validators=[registration.validators.validate_phone_number, registration.validators.validate_positive_number], verbose_name='phone number')),
                ('age', models.PositiveSmallIntegerField(validators=[registration.validators.validate_age, registration.validators.validate_positive_number], verbose_name='age')),
                ('experience', models.PositiveSmallIntegerField(verbose_name='experience')),
                ('operating_system', models.CharField(choices=[['Wndws', 'Windows'], ['Lnx', 'Linux'], ['MO', 'MacOS']], max_length=200, verbose_name='operating system')),
                ('programs', models.CharField(max_length=200, verbose_name='programs')),
                ('comp_games', models.CharField(max_length=200, verbose_name='computer games')),
                ('comp_hardware', models.CharField(choices=[['PC', 'Personal Computer'], ['LP', 'Laptop']], max_length=100, verbose_name='computer hardware')),
                ('sources', models.CharField(choices=[['inst', 'Instagram'], ['TT', 'TikTok'], ['WS', 'Web Sites'], ['O', 'Other']], max_length=100, verbose_name='sources')),
                ('profession', models.CharField(max_length=250, verbose_name='profession')),
                ('target', models.CharField(max_length=250, verbose_name='target')),
                ('ideas', models.TextField(blank=True, null=True, verbose_name='ideas')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]