# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from apps.common.models import *


__author__ = 'ngnono'


class CategoryEntity(DataBaseEntity):
    Name = models.CharField(max_length=256)
    Description = models.TextField()
    PrentId = models.IntegerField()
    Level = models.IntegerField()
    Type = models.IntegerField()
    # SecondName = models.CharField(max_length=256)

    User = models.OneToOneField(User)

    class Meta:
        db_table = "Category"