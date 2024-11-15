# Generated by Django 4.2.7 on 2023-12-19 16:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_remove_bsb_file_remove_chsb_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bsb',
            name='grade_number',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='exam.grade'),
        ),
        migrations.AddField(
            model_name='chsb',
            name='grade_number',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='exam.grade'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='grade_num',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(11)]),
        ),
    ]
