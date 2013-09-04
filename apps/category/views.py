# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from apps.bill.models import CategoryEntity
from apps.category.forms import CategoryForm
from apps.category.serializer import CategorySerializer
from apps.common.models import ExecStatus, ExecResult
from apps.common.serializer import JSONResponse, ExecResultSerializer
from apps.common.wrapper import csrfWrapper

__author__ = 'ngnono'


def getlist(request):
    user = request.user

    # if user is not None:
    #     queryset = CategoryEntity.objects.filter(User_id=user.id)
    #
    # else:
    q = request.GET.get('q')
    queryset = CategoryEntity.objects.filter(Name__contains=q)

    serializer = CategorySerializer(queryset, many=True)

    return JSONResponse(serializer.data)


def getItem(id):
    return CategoryEntity.objects.get(id)


def detail(request, id):
    item = getItem(id)

    return render_to_response("web4mobile/category/detail.html", locals())


def create(request, *args, **kwargs):
    if request.method == "GET":
        return create_get(request, *args, **kwargs)
    else:
        return create_post(request, *args, **kwargs)


@csrfWrapper
def create_get(request, csrf_token):
    # csrf_token = _get_new_csrf_key()
    # request.csrf_processing_done = False
    # request.META['CSRF_COOKIE'] = csrf_token
    # request.META['CSRF_COOKIE_USED'] = True
    return render_to_response("web4mobile/category/create.html", locals())


def create_post(request, *args, **kwargs):
    form = CategoryForm(request.POST or None)

    if form.is_valid():
        item = form.save()

        result = ExecResult(item, msg="创建成功", status=ExecStatus.Success)
        serializer = ExecResultSerializer(result)
        return JSONResponse(serializer.data, status=200)
        # return render_to_response("web4mobile/category/update.html", locals())
    else:
        # return render_to_response("web4mobile/category/create.html", locals())
        result = ExecResult(form.errors, msg="验证参数错误", status=ExecStatus.ClientError)
        serializer = ExecResultSerializer(result)
        return JSONResponse(serializer.data, status=200)


def update(request):
    pass


def delete(request, id):
    item = getItem(id)

    CategoryEntity.delete(item)

