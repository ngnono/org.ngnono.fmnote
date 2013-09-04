# -*- coding:utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from apps.common.wrapper import http_post, http_get

__author__ = 'ngnono'


@http_get
def login_view(request):
    pass


@http_post
def login_handler(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])

    if user is not None:
        login(request, user)


def login(request):
    pass


def logout_view(request):
    logout(request)
    pass