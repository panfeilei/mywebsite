# Generated by Django 2.0 on 2018-07-10 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20180710_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='authorId',
            field=models.ForeignKey(db_column='authorId', on_delete=django.db.models.deletion.CASCADE, related_name='userbloglist', to=settings.AUTH_USER_MODEL),
        ),
    ]
