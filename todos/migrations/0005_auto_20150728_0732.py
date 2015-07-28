# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0004_auto_20150728_0705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('due', models.DateTimeField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('done', models.BooleanField(default=False)),
                ('color', models.CharField(default=b'yellow', max_length=50)),
                ('fontcolor', models.CharField(default=b'black', max_length=50)),
                ('folder', models.ForeignKey(related_name='notes', blank=True, to='todos.Folder', null=True)),
                ('tag', models.ManyToManyField(related_name='notes', null=True, to='todos.Tag', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='todo',
            name='folder',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='tag',
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
