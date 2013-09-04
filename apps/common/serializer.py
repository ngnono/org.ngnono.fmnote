# -*- coding:utf-8 -*-
from rest_framework import serializers
from apps.common.models import ExecResult

__author__ = 'ngnono'

from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer, XMLRenderer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders it's content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class XMLResponse(HttpResponse):
    """
    An HttpResponse that renders it's content into XML.
    """

    def __init__(self, data, **kwargs):
        content = XMLRenderer().render(data)
        kwargs['content_type'] = 'application/xml'
        super(XMLResponse, self).__init__(content, **kwargs)


class ExecResultSerializer(serializers.Serializer):
    """
    标准的返回类型
    """

    msg = serializers.CharField(required=False, max_length=100)
    data = serializers.CharField(required=False)
    status = serializers.IntegerField(required=False)
    isSuccess = serializers.BooleanField(required=False)
