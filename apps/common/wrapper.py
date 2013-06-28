# -*- coding:utf-8 -*-
from django.http import request
from django.views.decorators.csrf import csrf_exempt

__author__ = 'ngnono'


class httpMethod(object):
    POST = 1
    GET = 2
    PUT = 3
    DELETE = 4


class httpMethodException(Exception):
    pass


def http_post(func):
    def wrapper(*args, **kwargs):
        if request.method == "POST":
            ret = func(*args, **kwargs)
            return ret
        else:
            raise httpMethodException

    return wrapper


def http_method(httpMethod):
    """

    :param httpMethod:  httpMethod
    :return: :raise:
    """

    def _http_method(func):
        def wrapper(*args, **kwargs):
            if request.method == httpMethod:
                ret = func(*args, **kwargs)

                return ret
            else:
                raise httpMethodException

        return wrapper

    return _http_method