# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('todos', '0006_auto_20150817_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='user',
            field=models.ForeignKey(blank=True, to='accounts.UserProfile', null=True),
            preserve_default=True,
        ),
    ]
