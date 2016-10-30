# -*- coding: utf8 -*-
from __future__ import unicode_literals

from flask import Blueprint, request, url_for
from flask_login import login_required, current_user

from . import res
from models.resource import Resource, Content, Tag
from errors import Errors
from utils.datetime_utils import now_lambda

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


@instance.route('/article/index', methods=['POST'])
def article_index():
    """
    文章列表
    page              页
    from_id           分类（0:全部 1:hj's world 2:fashion）
    tag_id            标签ID
    :return:
    """

    conditions = {}
    from_id = request.form.get('from_id', 0, int)
    if from_id:
        conditions.update(from_id=from_id)

    tag_id = request.form.get('tag_id')
    if tag_id:
        conditions.update(tags=tag_id)

    page = request.form.get('page', 1, int)

    cs = Content.objects(**conditions).order_by('-created_at')
    per_page = 10
    total = cs.count()
    data = [c.as_dict() for c in cs[per_page * (page - 1): per_page * page]]
    return res(data=dict(data=data, page=page, total=total))


@instance.route('/article/details', methods=['POST'])
def article_details():
    """
    文章列表详情
    content_id          # 文章ID
    :return:
    """

    content_id = request.form.get('content_id')
    if not content_id:
        return res(Errors.PARAMS_REQUIRED)

    c = Content.objects(id=content_id, deleted_at=None).first()
    if not c:
        return res(Errors.NOT_FOUND)

    pre = Content.objects(created_at__gt=c.created_at).order_by('created_at').first()
    next = Content.objects(created_at__lt=c.created_at).order_by('-created_at').first()

    return res(data=dict(data=c.as_dict(),
                         pre_data=pre.as_dict() if pre else None,
                         next_data=next.as_dict() if next else None))


@instance.route('/article/edit', methods=['POST'])
@login_required
def article_edit():
    """
    文章新建/编辑
    content_id          # 文章ID  （可选, 编辑时必传）
    title               # 文章标题
    text                # 内容
    author_id           # 作者
    from_id             # 大分类
    tags                # 标签ID列表
    :return:
    """

    content_id = request.form.get('content_id')
    if not content_id:
        return res(Errors.PARAMS_REQUIRED)

    title = request.form.get('title')
    if not title:
        return res(Errors.PARAMS_REQUIRED)

    text = request.form.get('text')
    if not text:
        return res(Errors.PARAMS_REQUIRED)

    from_id = request.form.get('from_id')
    if not from_id:
        return res(Errors.PARAMS_REQUIRED)

    tags = request.form.getlist('tags[]', [])
    if not tags:
        return res(Errors.PARAMS_REQUIRED)

    c = Content.objects(id=content_id, deleted_at=None).first()
    if not c:
        c = Content()

    c.title = title
    c.text = text
    c.author_id = current_user.id
    c.from_id = from_id
    c.tags = tags
    c.save()
    return res(data=c.as_dict())


@instance.route('/article/delete', methods=['POST'])
@login_required
def article_delete():
    """
    删除文章
    article_id         文章ID   （可选, 编辑时必填）
    :return:
    """
    article_id = request.form.get('article_id')
    if not article_id:
        return res(Errors.PARAMS_REQUIRED)


    c = Content.objects(id=article_id, deleted_at=None).first()
    if not c:
        return res(Errors.NOT_FOUND)

    c.deleted_at = now_lambda()
    c.save()
    return res()


@instance.route('/tags/index', methods=['POST'])
def tag_index():
    """
    标签加载
    :return:
    """

    ts = Tag.objects(deleted_at=None)
    data = [t.as_dict() for t in ts]
    return res(data=data)


@instance.route('/tags/edit', methods=['POST'])
@login_required
def tag_edit():
    """
    新建/编辑标签
    tag_id         标签ID   （可选, 编辑时必填）
    name           标签名
    :return:
    """
    tag_id = request.form.get('tag_id')
    if not tag_id:
        return res(Errors.PARAMS_REQUIRED)

    name = request.form.get('name')
    if not name:
        return res(Errors.PARAMS_REQUIRED)

    t = Tag.objects(id=tag_id, deleted_at=None).first()
    if not t:
        t = Tag()

    t.name = name
    t.save()
    return res(data=t.as_dict())


@instance.route('/tags/delete', methods=['POST'])
@login_required
def tag_delete():
    """
    删除标签
    tag_id         标签ID   （可选, 编辑时必填）
    name           标签名
    :return:
    """
    tag_id = request.form.get('tag_id')
    if not tag_id:
        return res(Errors.PARAMS_REQUIRED)


    t = Tag.objects(id=tag_id, deleted_at=None).first()
    if not t:
        return res(Errors.NOT_FOUND)

    t.deleted_at = now_lambda()
    t.save()
    return res()








