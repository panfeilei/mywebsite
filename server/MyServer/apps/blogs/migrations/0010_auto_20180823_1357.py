# Generated by Django 2.0 on 2018-08-23 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_auto_20180821_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='descript',
            field=models.CharField(max_length=200, null=True),
        ),
    ]