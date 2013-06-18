# -*- coding:utf-8 -*-
__author__ = 'ngnono'

from django.db import models
from django.contrib.auth.models import User

from apps.common.models import *


class UserProfile(DataBaseEntity):
    User = models.OneToOneField(User)

    def __unicode__(self):
        return "user profile"

    class Meta:
        db_table = "UserProfile"


class CategoryEntity(DataBaseEntity):
    Name = models.CharField(max_length=64)
    Description = models.TextField()
    PrentId = models.IntegerField()
    Level = models.IntegerField()
    Type = models.IntegerField()

    User = models.OneToOneField(User)

    class Meta:
        db_table = "Category"


class TagEntity(DataBaseEntity):
    Name = models.CharField(max_length=64)
    Description = models.TextField()
    Type = models.IntegerField()

    User = models.OneToOneField(User)

    class Meta:
        db_table = "Tag"


class BillEntity(DataBaseEntity):
    Title = models.CharField(max_length=128)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    EntryDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    Type = models.SmallIntegerField()

    User = models.OneToOneField(User)
    Category = models.OneToOneField(CategoryEntity)
    Tags = models.ManyToManyField(TagEntity, through="BillTagRelationship")

    class Meta:
        db_table = "Bill"


class BillTagRelationship(BaseEntity):
    Bill = models.ForeignKey(BillEntity)
    Tag = models.ForeignKey(TagEntity)
    CreatedDate = models.DateField(auto_now_add=True, auto_now=False)
    CreatedUser = models.IntegerField()

    class Meta:
        db_table = "BillTagRelationship"


class BillType(EnumBase):
    Default = 0
    Expenditure = 2
    Revenue = 1