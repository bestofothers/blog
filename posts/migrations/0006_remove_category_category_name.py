# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20150505_0608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_name',
        ),
    ]
