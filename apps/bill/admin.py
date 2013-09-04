# -*- coding:utf-8 -*-
from django.contrib import admin
from apps.bill import models

__author__ = 'ngnono'


class BillAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.BillEntity, BillAdmin)