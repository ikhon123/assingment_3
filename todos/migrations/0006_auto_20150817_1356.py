# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0005_auto_20150728_0732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='fontcolor',
        ),
        migrations.RemoveField(
            model_name='note',
            name='fontcolor',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='fontcolor',
        ),
    ]
