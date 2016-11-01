# -*- coding: utf8 -*-
from __future__ import unicode_literals
import os
import time
import mimetypes
from threading import Thread

from flask_mail import Message

from app import mail
from manage import rosehj


def get_mimetype(filename):
    ext = os.path.splitext(filename)[-1]
    return mimetypes.types_map.get(ext)


def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper


class Email(Message):
    def __init__(self, send_email, recipients, sender=None, subject='', body=None, html=None):
        super(Email, self).__init__(subject=subject, sender=(sender or '匿名', send_email), recipients=recipients,
            date=time.time(), body=body, html=html)

    def add_attachment_with_filepath(self, file_path, send_file_name=None):
        mytype = get_mimetype(file_path) or 'text/plain'
        with open(file_path, 'rb') as f:
            self.attach(u'{0}'.format(send_file_name or '未命名'), mytype, f.read())

    def add_attachment_with_io(self, io, ext, send_file_name=None):
        io.seek(0)
        mytype = mimetypes.types_map.get('.' + ext) or 'text/plain'
        self.attach(u'{0}'.format(send_file_name or '未命名'), mytype, io.read())
        io.close()

    @async
    def send_email(self):
        with rosehj.app_context():
            mail.send(self)
