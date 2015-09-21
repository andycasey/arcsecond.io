# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import multiselectfield.db.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('arcsecond', '0007_observingsite_acronym'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObservingSiteActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, null=True, blank=True)),
                ('action', models.CharField(default=b'unk', max_length=10, choices=[(b'unk', b'(Undefined)'), (b'load', b'loaded'), (b'prop', b'changed property'), (b'del', b'deleted site')])),
                ('property_name', models.CharField(max_length=200, null=True)),
                ('old_value', models.CharField(max_length=200, null=True)),
                ('new_value', models.CharField(max_length=200, null=True)),
                ('action_message', models.CharField(max_length=1000, null=True)),
                ('method', models.CharField(default=b'unk', max_length=10, choices=[(b'unk', b'unk'), (b'db', b'db'), (b'django', b'django'), (b'api', b'api'), (b'web', b'web')])),
            ],
        ),
        migrations.AddField(
            model_name='observingsite',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='observingsite',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='observingsite',
            name='sources',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=36, null=True, choices=[(b'(Undefined)', b'(Undefined)'), (b'User', b'User'), (b'iObserve', b'iObserve'), (b'Xephem', b'Xephem'), (b'MPC', b'MPC')]),
        ),
        migrations.AddField(
            model_name='observingsiteactivity',
            name='observing_site',
            field=models.OneToOneField(null=True, blank=True, to='arcsecond.ObservingSite'),
        ),
        migrations.AddField(
            model_name='observingsiteactivity',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
