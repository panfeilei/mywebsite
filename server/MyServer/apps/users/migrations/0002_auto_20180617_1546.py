# Generated by Django 2.0 on 2018-06-17 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmessage',
            name='toUser',
        ),
        migrations.RemoveField(
            model_name='blogmessage',
            name='user',
        ),
        migrations.RemoveField(
            model_name='systemmessage',
            name='toUser',
        ),
        migrations.RemoveField(
            model_name='usermessage',
            name='toUser',
        ),
        migrations.RemoveField(
            model_name='usermessage',
            name='user',
        ),
        migrations.DeleteModel(
            name='BlogMessage',
        ),
        migrations.DeleteModel(
            name='SystemMessage',
        ),
        migrations.DeleteModel(
            name='UserMessage',
        ),
    ]
