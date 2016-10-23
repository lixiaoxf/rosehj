# -*- coding: utf8 -*-
from __future__ import unicode_literals

from mongoengine import StringField, IntField
from flask import url_for

from . import BaseDocument, register_pre_save
from configs.config import conf


@register_pre_save()
class Resource(BaseDocument):
    IMAGE = 1
    VIDEO = 2

    # 上传文件格式设置
    ALLOWED_FORMATS = ['jpg', 'png', 'jpeg', 'gif', 'rm', 'rmvb', 'wmv', 'avi', 'mp4', '3gp', 'mkv']

    # 上传文件大小上线
    ALLOWED_MAX_SIZE = 200 * 1024 ** 2  # 200M

    RESOURCE_TYPE = [
        (IMAGE, '图片'),
        (VIDEO, '视频')
    ]

    name = StringField()
    type = IntField(choices=RESOURCE_TYPE)
    file_id = StringField()

    meta = {
        'collection': 'resource',
        'db_alias': conf.DATABASE_NAME,
        'strict': False
    }

    def as_dict(self):
        dic = dict(self.to_mongo())
        dic['url'] = url_for('file.show', file_id=self.file_id)
        return dic