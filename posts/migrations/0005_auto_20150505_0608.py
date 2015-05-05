# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20150430_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(populate_from=(b'category_name',), editable=False, blank=True, unique=True, verbose_name=b'slug'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(populate_from=(b'title',), editable=False, blank=True, unique=True, verbose_name=b'slug'),
        ),
    ]
