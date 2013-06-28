# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from apps.bill.models import CategoryEntity
from apps.category.forms import CategoryForm
from apps.category.serializer import CategorySerializer
from apps.common.serializer import JSONResponse

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


@csrf_exempt
def create(request):
    if request.method == "GET":
        return create_get(request)
    else:
        return create_post(request)


def create_get(request):
    return render_to_response("web4mobile/category/create.html", locals())


def create_post(request):
    form = CategoryForm(request.POST or None)

    if form.is_valid():
        item = form.save()

        return render_to_response("web4mobile/category/update.html", locals())
    else:
        return render_to_response("web4mobile/category/create.html", locals())


def update(request):
    pass


def delete(request, id):
    item = getItem(id)

    CategoryEntity.delete(item)

