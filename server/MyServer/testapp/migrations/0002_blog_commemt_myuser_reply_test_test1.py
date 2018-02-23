# Generated by Django 2.0.2 on 2018-02-23 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('link', models.URLField()),
                ('descript', models.CharField(max_length=100, null=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='test1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Commemt',
            fields=[
                ('comment_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='testapp.Blog')),
                ('username', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('headimg', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('reply_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='testapp.Commemt')),
                ('username', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('headimg', models.CharField(max_length=50)),
                ('to', models.CharField(max_length=20)),
            ],
        ),
    ]