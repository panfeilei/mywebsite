# Generated by Django 2.0.5 on 2018-05-06 07:12

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('userId', models.IntegerField(default=0, unique=True)),
                ('headlink', models.CharField(default='/', max_length=50)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('link', models.URLField()),
                ('descript', models.CharField(max_length=100, null=True)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('to_blogId', models.CharField(max_length=50)),
                ('time', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('userid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('reply_id', models.AutoField(primary_key=True, serialize=False)),
                ('to_commentId', models.IntegerField()),
                ('to_blogId', models.CharField(max_length=50)),
                ('to_username', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('userid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='testmedel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
