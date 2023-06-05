# Generated by Django 3.1.14 on 2023-06-05 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0015_auto_20230604_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Название анг.'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Название яп.'),
        ),
    ]
