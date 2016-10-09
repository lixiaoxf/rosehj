# -*- coding: utf8 -*-
from __future__ import unicode_literals
from functools import wraps

from flask import jsonify

from errors import Errors


def res(code=Errors.SUCCESS, data=None, error=None, extra_msg=None):
    result = {
        'code': code,
    }
    if Errors.is_succeed(code):
        result['success'] = True
        result['detail'] = data
    else:
        result['success'] = False
        if error:
            result['error'] = error
        else:
            result['error'] = Errors.error_msg(code, extra_msg)
    return jsonify(**result)
