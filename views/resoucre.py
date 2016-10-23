# -*- coding: utf8 -*-
from __future__ import unicode_literals

from flask import Blueprint, request, url_for

from . import res
from models.resource import Resource
from errors import Errors

instance = Blueprint('resource', __name__)


@instance.before_request
def before_request():
    pass


@instance.route('/resource/edit', methods=['POST'])
def edit():
    """
    新建/编辑资源
    name      文件名
    file_id   上传的文件ID
    type      文件类型
    :return:
    """
    name = request.form.get('name')
    type = request.form.get('type')
    file_id = request.form.get('file_id')
    if not name or not type or not file_id:
        return res(code=Errors.PARAMS_REQUIRED)

    if type not in Resource.RESOURCE_TYPE:
        return res(code=Errors.UPLOAD_FORMAT_LIMITATION)

    r = Resource.objects(file_id=file_id).first()
    if not r:
        r = Resource()
    r.name = name
    r.type = type
    r.file_id = file_id
    r.save()
    return res(data=r.as_dict())


