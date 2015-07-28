# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_auto_20150728_0646'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='color',
            field=models.CharField(default=b'purple', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='folder',
            name='fontcolor',
            field=models.CharField(default=b'white', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tag',
            name='color',
            field=models.CharField(default=b'red', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tag',
            name='fontcolor',
            field=models.CharField(default=b'black', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todo',
            name='color',
            field=models.CharField(default=b'yellow', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todo',
            name='fontcolor',
            field=models.CharField(default=b'black', max_length=50),
            preserve_default=True,
        ),
    ]
