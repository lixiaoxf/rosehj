# -*- coding: utf8 -*-
from __future__ import unicode_literals


class Config(object):
    DEBUG = True
    SECRET_KEY = 'h!a@n#n$e%n^g&f*a(n)g_i+n.k'
    # 加密salt
    SALT = '*^)h#a&n@#$;.'

    # mongodb 链接信息
    DATABASE_NAME = 'rosehj'
    DATABASE_HOST = '127.0.0.1'
    DATABASE_PORT = 27017
    DATABASE_USERNAME = 'root'
    DATABASE_PASSWORD = 'rosehj'
    DATABASE_URL = 'mongodb://{0}:{1}@{2}:{3}'.format(DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT)

conf = Config