# -*- coding: utf-8 -*-
import os
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.conf import settings
from django.views.generic.base import View
from .forms import LoginForm
from .models import UserProfile


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', "")
            password = request.POST.get('password'"")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.backend == 'users.authentication.EmailAuthBackend':
                        up = UserProfile.objects.get(email=username)
                    else:
                        up = UserProfile.objects.get(username=username)

                    return render(request, 'index.html',
                                  {'username': username, 'image': up.image.url})
                else:
                    return render(request, 'login.html', {"msg": "用户未激活"})
            else:
                return render(request, 'login.html', {"msg": "用户名或者密码错误"})
        else:
            return render(request, 'login.html', {"msg": "", "login_form": login_form})


def mylogout(request):
    logout(request)
    return render(request, 'index.html', {'username': '', 'image': ''})


def register(request):
    pass
