# Generated by Django 2.0 on 2018-06-18 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0004_auto_20180618_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmessage',
            name='toUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BlogtoUser', to='users.UserInfo'),
        ),
        migrations.AlterField(
            model_name='blogmessage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BlogUser', to='users.UserInfo'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favo_list', to='users.UserInfo'),
        ),
        migrations.AlterField(
            model_name='interest',
            name='toUserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserInfo'),
        ),
        migrations.AlterField(
            model_name='interest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inter_list', to='users.UserInfo'),
        ),
        migrations.AlterField(
            model_name='systemmessage',
            name='toUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserInfo'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='toUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ToUser', to='users.UserInfo'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FromUser', to='users.UserInfo'),
        ),
    ]
