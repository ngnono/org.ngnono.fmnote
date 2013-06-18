# -*- coding:utf-8 -*-
from django.contrib.auth import authenticate, login, logout

__author__ = 'ngnono'


def login_view(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])

    if user is not None:
        login(request, user)
    pass


def logout_view(request):
    logout(request)
    pass