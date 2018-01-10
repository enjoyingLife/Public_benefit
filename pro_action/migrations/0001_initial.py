# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userproject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('card_pic', models.CharField(max_length=100)),
                ('data_file', models.CharField(max_length=100)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('is_success', models.BooleanField(default=False)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'apply',
            },
        ),
        migrations.CreateModel(
            name='Cate',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'cate',
            },
        ),
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('is_success', models.BooleanField(default=False)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'join',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('pro_action', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('pro_cate', models.ForeignKey(to='pro_action.Cate')),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.AddField(
            model_name='join',
            name='join_action',
            field=models.ForeignKey(to='pro_action.Project'),
        ),
        migrations.AddField(
            model_name='join',
            name='join_user',
            field=models.ForeignKey(to='user.User'),
        ),
        migrations.AddField(
            model_name='apply',
            name='apply_project',
            field=models.ForeignKey(to='pro_action.Project'),
        ),
        migrations.AddField(
            model_name='apply',
            name='apply_user',
            field=models.ForeignKey(to='user.User'),
        ),
    ]
