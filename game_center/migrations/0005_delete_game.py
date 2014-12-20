# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_center', '0004_auto_20141124_0309'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Game',
        ),
    ]
