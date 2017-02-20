# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
from django.db import migrations


def forwards_func(apps, schema_editor):
    Meeting = apps.get_model("moim", "Meeting")
    db_alias = schema_editor.connection.alias
    Meeting.objects.using(db_alias).bulk_create([
        Meeting(maker="장선혁", name="규카츠 먹을래?", place="강남", start_time="2017-02-19T08:09:29Z",
                image_path="", distance_near_univ="고려대학교 10km 이내", price_range="233000원~335000원"),
    ])


def reverse_func(apps, schema_editor):
    Meeting = apps.get_model("moim", "Meeting")
    db_alias = schema_editor.connection.alias
    Meeting.objects.using(db_alias).filter(name="돈까스 모임2").delete()


class Migration(migrations.Migration):

    dependencies = [
        ('moim', '0002_auto_20170219_0812'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
