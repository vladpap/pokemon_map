# Generated by Django 3.1.14 on 2023-06-01 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0009_auto_20230601_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
