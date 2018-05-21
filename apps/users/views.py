# -*- coding: utf-8 -*-
import os
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.conf import settings
from .forms import LoginForm
from .models import UserProfile


def mylogout(request):
    logout(request)
    return render(request, 'index.html', {'username': '', 'image': ''})


def mylogin(request):
    return _trylogin(request)
    # form = _trylogin(request)
    # return render(request, 'login.html', {'form': form})


def _trylogin(request):
    if request.method == 'POST':
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
                              {'username': username, 'image': os.path.join(settings.MEDIA_URL, up.image.name)})
            else:
                return render(request, 'login.html', {"msg": "用户未激活"})
        else:
            return render(request, 'login.html', {"msg": "用户名或者密码错误"})
    else:
        return render(request, 'login.html', {})


def _trylogin1(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    mylogin(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return form


def register(request):
    pass
