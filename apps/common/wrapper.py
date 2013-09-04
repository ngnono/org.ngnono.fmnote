# -*- coding:utf-8 -*-
from django.middleware.csrf import _get_new_csrf_key

__author__ = 'ngnono'


class httpMethod(object):
    POST = 1
    GET = 2
    PUT = 3
    DELETE = 4


class HttpMethodException(Exception):
    def __init__(self, msg):
        Exception.__init__(self)
        self.message = msg


class CsrfWrapperException(Exception):
    def __init__(self, msg):
        self.message = msg


def http_post(func):
    def wrapper(request, *args, **kwargs):
        if request.method == httpMethod.POST:
            ret = func(request, *args, **kwargs)
            return ret
        else:
            raise HttpMethodException(u"只接受post方法")

    return wrapper


def http_get(func):
    def wrapper(request, *args, **kwargs):
        if request.method == httpMethod.GET:
            ret = func(request, *args, **kwargs)
            return ret
        else:
            raise HttpMethodException(u"只接受GET方法")

    return wrapper


def http_method(httpMethod):
    """

    :param httpMethod:  GET POST
    :return: :raise:
    """

    def _http_method(func):
        def wrapper(request, *args, **kwargs):
            if request.method == httpMethod:
                ret = func(request, *args, **kwargs)

                return ret
            else:
                raise httpMethodException

        return wrapper

    return _http_method


def csrfWrapper(func):
    """
    csrf dj middleware help method
    need add attribute on the methods
    need add params csrf_token in view method params

    e:
    @csrfWrapper
    def create_get(request, csrf_token ):

    """

    def wrapper(request, *args, **kwargs):
        if request.method == "GET":
            csrf_token = _get_new_csrf_key()
            request.csrf_processing_done = False
            request.META['CSRF_COOKIE'] = csrf_token
            request.META['CSRF_COOKIE_USED'] = True
            kwargs["csrf_token"] = csrf_token

            ret = func(request, *args, **kwargs)

            return ret
        else:
            raise CsrfWrapperException("csrf 只能装饰在GET方法上")

    return wrapper