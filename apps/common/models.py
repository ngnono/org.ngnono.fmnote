# -*- coding:utf-8 -*-
__author__ = 'ngnono'

from django.db import models


# Create your models here.

class BaseEntity(models.Model):
    Id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True


class DataBaseEntity(BaseEntity):
    CreatedDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    CreatedUser = models.IntegerField()
    UpdatedDate = models.DateTimeField(auto_now=True, auto_now_add=True)
    UpdatedUser = models.IntegerField()
    Status = models.IntegerField()
    IsDeleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class EnumBase(object):
    pass


class ExecStatus(object):
    Success = 200
    ClientError = 410
    ServerError = 500


class ExecResult(object):
    def __init__(self, *args, **kwargs):
        self.status = kwargs["status"]
        self.msg = kwargs["msg"]
        self.data = args
        self.isSuccess = self.status == 200

    class Meta:
        pass