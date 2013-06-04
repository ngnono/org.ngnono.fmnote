# -*- coding:utf-8 -*-
__author__ = 'ngnono'

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BassEntity(models.Model):
    class Meta:
        abstract = True


class DataBaseEntity(BassEntity):
    CreatedDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    CreatedUser = models.IntegerField()
    UpdatedDate = models.DateTimeField(auto_now=True, auto_now_add=True)
    UpdatedUser = models.IntegerField()
    Status = models.IntegerField()
    IsDeleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class UserProfile(DataBaseEntity):
    User = models.OneToOneField(User)

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

    User = models.OneToOneField(User)
    Category = models.OneToOneField(CategoryEntity)
    Tags = models.ManyToManyField(TagEntity)

    class Meta:
        db_table = "Bill"