# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_remove_category_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_name',
            field=models.CharField(default=1, unique=True, max_length=200),
            preserve_default=False,
        ),
    ]
