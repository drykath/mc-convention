# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('short_name', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=4)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('active', models.BooleanField(default=False)),
                ('contact_email', models.EmailField(max_length=254)),
                ('site', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='sites.Site')),
            ],
        ),
    ]
