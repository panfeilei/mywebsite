# Generated by Django 2.0.2 on 2018-02-26 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20180225_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='to_blogId',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='to_blogId',
            field=models.CharField(max_length=50),
        ),
    ]