# Generated by Django 4.2.7 on 2023-11-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_book_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(default='Book none found', max_length=255),
        ),
    ]
