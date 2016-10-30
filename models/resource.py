# -*- coding: utf8 -*-
from __future__ import unicode_literals

from mongoengine import StringField, IntField, ListField, EmbeddedDocumentField, EmbeddedDocument, DateTimeField, \
    BooleanField
from flask import url_for

from . import BaseDocument, register_pre_save
from configs.config import conf
from utils.datetime_utils import format_datetime


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
        if 'created_at' in dic:
            del dic['created_at']
        if 'updated_at' in dic:
            del dic['updated_at']
        if 'deleted_at' in dic:
            del dic['deleted_at']
        dic['url'] = url_for('file.show', file_id=self.file_id)
        return dic


class EmbedComment(EmbeddedDocument):
    comment = StringField()
    nickname = StringField()
    email = StringField()
    notify = BooleanField(default=False)
    created_at = DateTimeField()

    def as_dict(self):
        dic = dict(self.to_mongo())
        dic['created_at'] = format_datetime(self.created_at, '%b %d, %Y')
        return dic


@register_pre_save()
class Tag(BaseDocument):
    name = StringField(required=True)

    meta = {
        'collection': 'tag',
        'db_alias': conf.DATABASE_NAME,
        'strict': False
    }

    def as_dict(self):
        dic = dict(self.to_mongo())
        if 'created_at' in dic:
            del dic['created_at']
        if 'updated_at' in dic:
            del dic['updated_at']
        if 'deleted_at' in dic:
            del dic['deleted_at']
        return dic


@register_pre_save()
class Content(BaseDocument):
    FROM_HJ_WORLD = 1
    FROM_FASHION = 2
    FROM_IDS = [
        (FROM_HJ_WORLD, 'HJ\'S WORLD'),
        (FROM_FASHION, 'FASHION')
    ]

    title = StringField()  # 标题
    text = StringField()  # 内容
    author_id = StringField()  # 作者
    from_id = IntField(default=FROM_HJ_WORLD, choices=FROM_IDS)  # 来源
    tags = ListField(StringField(), default=[])
    comments = ListField(EmbeddedDocumentField(EmbedComment), default=[])

    meta = {
        'collection': 'content',
        'db_alias': conf.DATABASE_NAME,
        'strict': False
    }

    def as_dict(self):
        dic = dict(self.to_mongo())
        comments = []
        for comment in self.comments:
            comments.append(comment.as_dict())
        dic['comments'] = comments
        dic['created_at'] = format_datetime(self.created_at, '%b %d, %Y')
        return dic