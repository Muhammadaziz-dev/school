# Generated by Django 4.2.7 on 2023-12-19 03:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BSB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='exam/bsb/')),
                ('bsb_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CHSB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='exam/chsb/')),
                ('chsb_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('bsb', models.ManyToManyField(to='exam.bsb')),
                ('chsb', models.ManyToManyField(to='exam.chsb')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_number', models.PositiveSmallIntegerField(null=True, unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(11)])),
                ('subjects', models.ManyToManyField(to='exam.subject')),
            ],
        ),
    ]
