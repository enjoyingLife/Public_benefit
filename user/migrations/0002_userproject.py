# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProject',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('user_id', models.IntegerField()),
                ('project_id', models.IntegerField()),
                ('grade', models.IntegerField()),
                ('money', models.DecimalField(decimal_places=2, max_digits=12)),
                ('goods', models.CharField(max_length=100)),
                ('is_attention', models.NullBooleanField(default=None)),
                ('is_join', models.NullBooleanField(default=None)),
                ('is_help', models.NullBooleanField(default=None)),
                ('is_apply', models.NullBooleanField(default=None)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'user_project',
            },
        ),
    ]
