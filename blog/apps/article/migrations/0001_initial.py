# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-10 11:15
from __future__ import unicode_literals

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('excerpt', models.CharField(blank=True, max_length=200, null=True, verbose_name='简介')),
                ('pic', models.ImageField(upload_to='Article_img/%Y/%m', verbose_name='图片')),
                ('content', ckeditor.fields.RichTextField(verbose_name='内容')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('modified_time', models.DateTimeField(verbose_name='修改时间')),
                ('on_click', models.IntegerField(default=0, verbose_name='点击量')),
                ('comment_num', models.IntegerField(default=0, verbose_name='评论量')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name_plural': '文章',
                'db_table': 'Article',
                'verbose_name': '文章',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='分类')),
            ],
            options={
                'verbose_name_plural': '分类',
                'db_table': 'Category',
                'verbose_name': '分类',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标签')),
            ],
            options={
                'verbose_name_plural': '标签',
                'db_table': 'Tag',
                'verbose_name': '标签',
            },
        ),
    ]
