# Generated by Django 2.0.2 on 2018-02-25 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20180225_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='userid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='userid',
            field=models.IntegerField(),
        ),
    ]
