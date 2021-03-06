# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-25 01:48
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20170803_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='封面图片'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='pushcontent',
            name='maincontent',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='正文'),
        ),
    ]
