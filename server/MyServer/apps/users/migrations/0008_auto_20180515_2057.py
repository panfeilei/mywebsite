# Generated by Django 2.0.5 on 2018-05-15 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180515_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='fromBlog',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='unreadmessage',
            name='fromBlog',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
