# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('atitle', models.CharField(verbose_name='名称', max_length=20)),
                ('aParent', models.ForeignKey(to='user.AreaInfo', blank=True, null=True)),
            ],
            options={
                'db_table': 'areas',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('pic', models.ImageField(upload_to='user')),
            ],
            options={
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('gender', models.BooleanField(default=True)),
                ('email', models.CharField(max_length=40)),
                ('birthday', models.DateField()),
                ('phone_num', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('user_areas', models.ForeignKey(to='user.AreaInfo')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
