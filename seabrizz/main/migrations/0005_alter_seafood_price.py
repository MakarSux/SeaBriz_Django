# Generated by Django 4.2.6 on 2023-12-20 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_image_seafood_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seafood',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
    ]
