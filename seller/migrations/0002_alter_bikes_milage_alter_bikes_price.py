# Generated by Django 4.0.4 on 2022-05-25 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikes',
            name='milage',
            field=models.FloatField(max_length=55),
        ),
        migrations.AlterField(
            model_name='bikes',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
