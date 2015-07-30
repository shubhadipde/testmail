# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailApp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(unique=True, max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('picture', models.ImageField(default=b'pic_folder/none', upload_to=b'pic_folder/')),
            ],
        ),
        migrations.AddField(
            model_name='emailapp',
            name='frm',
            field=models.ForeignKey(related_name='FromEmail', to='users.UserInfo'),
        ),
        migrations.AddField(
            model_name='emailapp',
            name='to',
            field=models.ForeignKey(related_name='ToEmail', to='users.UserInfo'),
        ),
    ]
