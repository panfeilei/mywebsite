# Generated by Django 2.0 on 2018-06-25 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180624_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='userId',
            field=models.OneToOneField(db_column='userId', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='UserInfo', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]