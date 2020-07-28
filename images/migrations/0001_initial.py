# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200, blank=True, null=True)),
                ('url', models.URLField()),
                ('slug', models.SlugField(max_length=200, blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('user', models.ForeignKey(related_name='images_created', to=settings.AUTH_USER_MODEL)),
                ('user_liked', models.ManyToManyField(blank=True, related_name='images_liked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
