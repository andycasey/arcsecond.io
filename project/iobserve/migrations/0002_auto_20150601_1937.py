# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('iobserve', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='astronomicalcoordinates',
            name='system',
            field=models.CharField(default=b'ICRS', max_length=20, choices=[(b'ICRS', b'ICRS'), (b'FK5', b'FK5'), (b'FK4', b'FK4'), (b'FK4NoETerms', b'FK4NoETerms'), (b'Galactic', b'Galactic'), (b'AltAz', b'AltAz')]),
        ),
        migrations.AddField(
            model_name='bibliographicreference',
            name='authors',
            field=models.ManyToManyField(related_name='authors', to='iobserve.Person'),
        ),
        migrations.AddField(
            model_name='bibliographicreference',
            name='bibcode',
            field=models.CharField(default=b'', max_length=18, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='bibliographicreference',
            name='title',
            field=models.CharField(default=b'', max_length=1000),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(default=b'', max_length=1000),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(default=b'', max_length=1000),
        ),
        migrations.AlterField(
            model_name='person',
            name='middle_name',
            field=models.CharField(default=b'', max_length=1000),
        ),
    ]
