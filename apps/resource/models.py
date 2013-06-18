# -*- coding:utf-8 -*-

from django.db import models
from apps.common.models import BaseEntity, DataBaseEntity

__author__ = 'ngnono'


class ResourceEntity(DataBaseEntity):
    SourceId = models.IntegerField()
    SourceType = models.IntegerField()
    Name = models.CharField(max_length=2048)
    IsDefault = models.BooleanField()
    SortOrder = models.IntegerField(default=0)
    Type = models.IntegerField()
    OrgExtName = models.CharField(max_length=16)
    # Unit Byte
    Size = models.BigIntegerField()
    # sencond
    Length = models.IntegerField()
    # px
    Width = models.IntegerField()
    # px
    Height = models.IntegerField()

    class Meta:
        db_table = "Resource"


class SourceType(object):
    pass


class ResourceType(object):
    Default = 0
    Image = 1
    Audio = 2
    Video = 3





