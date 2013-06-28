# -*- coding:utf-8 -*-
from rest_framework import serializers
from apps.bill.models import CategoryEntity

__author__ = 'ngnono'


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CategoryEntity
        fields = ("Id", "Name", "Description", "PrentId", "Level", "Type")
