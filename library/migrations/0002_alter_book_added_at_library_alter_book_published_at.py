# Generated by Django 5.1.2 on 2024-10-11 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='added_at_library',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='published_at',
            field=models.DateField(),
        ),
    ]
