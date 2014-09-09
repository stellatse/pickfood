# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('last_time', models.DateTimeField(auto_now=True)),
                ('picked_times', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShopList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
                ('verified', models.BooleanField(default=False)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('verified_time', models.DateTimeField(auto_now=True)),
                ('system', models.BooleanField(default=False)),
                ('role', models.IntegerField(default=0)),
                ('pay_account', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='shoplist',
            name='user',
            field=models.ForeignKey(to='picky.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shop',
            name='shop_list',
            field=models.ForeignKey(to='picky.ShopList'),
            preserve_default=True,
        ),
    ]
