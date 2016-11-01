# -*- coding: utf8 -*-
from __future__ import unicode_literals
import os
import glob

from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from werkzeug.routing import BaseConverter


from configs.config import conf
from models.user import User

mail = Mail()
login_manager = LoginManager()
# login_manager.session_protection = 'strong'
login_manager.login_view = 'index.index'
login_manager.login_message = '用户需要登录后方可访问该页面'


@login_manager.user_loader
def load_user(uid):
    return User.objects.with_id(uid)


class RegexConverter(BaseConverter):
    """
    添加url正则表达式判断方式
    用法@instance.route('/<regex("\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+"):email>')
    """
    def __init__(self, map, *args):
        self.map = map
        self.regex = args[0]


def __config_blueprint(app):
    dir = os.path.dirname(__file__)
    views_dir = os.path.join(dir, 'views')
    views_files = glob.glob(os.path.join(views_dir, '*.py'))
    for views_file in views_files:
        basename = os.path.basename(views_file)
        if basename == '__init__.py':
            continue

        views_file_name = basename[:basename.rindex('.')]
        module = __import__('views.{0}'.format(views_file_name), fromlist=['instance'])
        if not hasattr(module, 'instance'):
            continue

        instance = getattr(module, 'instance')
        app.register_blueprint(instance)


def create_app():
    app = Flask(__name__)

    mail.init_app(app)
    # 读配置文件
    app.config.from_object(conf)
    # flask扩展
    login_manager.init_app(app)
    # 添加正则url匹配转换器
    app.url_map.converters['regex'] = RegexConverter
    # 蓝图注册
    __config_blueprint(app)
    return app