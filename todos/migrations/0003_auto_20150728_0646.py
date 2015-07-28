# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20150714_0642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='todo',
            name='date',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='todo',
        ),
        migrations.AddField(
            model_name='todo',
            name='content',
            field=models.TextField(default=1, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todo',
            name='done',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todo',
            name='due',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todo',
            name='folder',
            field=models.ForeignKey(related_name='notes', blank=True, to='todos.Folder', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todo',
            name='tag',
            field=models.ManyToManyField(related_name='notes', null=True, to='todos.Tag', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todo',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
    ]
