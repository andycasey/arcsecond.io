# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0037_auto_20151115_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='astronomerstelegram',
            name='subjects',
            field=multiselectfield.db.fields.MultiSelectField(max_length=589, null=True, choices=[(b'unknown', b'unknown'), (b'Radio', b'Radio'), (b'Millimeter', b'Millimeter'), (b'Sub-Millimeter', b'Sub-Millimeter'), (b'Far-Infra-Red', b'Far-Infra-Red'), (b'Infra-Red', b'Infra-Red'), (b'Optical', b'Optical'), (b'Ultra-Violet', b'Ultra-Violet'), (b'X-ray', b'X-ray'), (b'Gamma Ray', b'Gamma Ray'), (b'>GeV', b'>GeV'), (b'TeV', b'TeV'), (b'VHE', b'VHE'), (b'UHE', b'UHE'), (b'Neutrinos', b'Neutrinos'), (b'A Comment', b'A Comment'), (b'AGN', b'AGN'), (b'Asteroid', b'Asteroid'), (b'Asteroid (Binary)', b'Asteroid (Binary)'), (b'Binary', b'Binary'), (b'Black Hole', b'Black Hole'), (b'Blazar', b'Blazar'), (b'Cataclysmic Variable', b'Cataclysmic Variable'), (b'Comet', b'Comet'), (b'Cosmic Rays', b'Cosmic Rays'), (b'Gamma-Ray Burst', b'Gamma-Ray Burst'), (b'Globular Cluster', b'Globular Cluster'), (b'Gravitational Waves', b'Gravitational Waves'), (b'Meteor', b'Meteor'), (b'Microlensing Event', b'Microlensing Event'), (b'Near-Earth Object', b'Near-Earth Object'), (b'Neutron Star', b'Neutron Star'), (b'Nova', b'Nova'), (b'Planet', b'Planet'), (b'Planet (minor)', b'Planet (minor)'), (b'Potentially Hazardous Asteroid', b'Potentially Hazardous Asteroid'), (b'Pre-Main-Sequence Star', b'Pre-Main-Sequence Star'), (b'Pulsar', b'Pulsar'), (b'Quasar', b'Quasar'), (b'Request for Observations', b'Request for Observations'), (b'Soft Gamma-ray Repeater', b'Soft Gamma-ray Repeater'), (b'Solar System Object', b'Solar System Object'), (b'Star', b'Star'), (b'Supernova Remnant', b'Supernova Remnant'), (b'Supernovae', b'Supernovae'), (b'The Sun', b'The Sun'), (b'Transient', b'Transient'), (b'Variables', b'Variables'), (b'Young Stellar Object', b'Young Stellar Object')]),
        ),
    ]
