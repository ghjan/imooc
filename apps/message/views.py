# -*- coding: utf-8 -*-
import pymysql

pymysql.install_as_MySQLdb()
from django.core.serializers.json import json

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import UserMessage


def getform(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        message = request.POST.get('message', '')
        user_message = UserMessage()
        user_message.name = name
        user_message.email = email
        user_message.address = address
        user_message.message = message
        user_message.save()
    else:
        all_messages = UserMessage.objects.filter(name='admin')
        message = UserMessage()
        if all_messages:
            message = all_messages[0]

        return render(request, "message_comment.html", {"my_message": message})
