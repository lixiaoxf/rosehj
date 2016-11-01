# -*- coding: utf8 -*-
from __future__ import unicode_literals


class Config(object):
    DEBUG = True
    SECRET_KEY = 'h!a@n#n$e%n^g&f*a(n)g_i+n.k'
    # 加密salt
    SALT = '*^)h#a&n@#$;.'

    MAIL_SERVER = 'smtp.126.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'ink_tech'
    MAIL_PASSWORD = 'mqhaner27'
    MAIL_DEFAULT_SENDER = None
    MAIL_MAX_EMAILS = 25
    MAIL_ASCII_ATTACHMENTS = True

    # mongodb 链接信息
    DATABASE_NAME = 'rosehj'
    DATABASE_HOST = '127.0.0.1'
    DATABASE_PORT = 27017
    DATABASE_USERNAME = 'root'
    DATABASE_PASSWORD = 'rosehj'
    DATABASE_URL = 'mongodb://{0}:{1}@{2}:{3}'.format(DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT)

conf = Config