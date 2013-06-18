# -*- coding:utf-8 -*-
from apps.bill.models import CategoryEntity

__author__ = 'ngnono'


def list(request):
    user = request.user

    if user is not None:
        taglist = CategoryEntity.objects.filter(User_Id=user.id)

    else:
        taglist = CategoryEntity.objects.filter(Type=1)



