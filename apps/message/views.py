# -*- coding: utf-8 -*-
import pymysql

pymysql.install_as_MySQLdb()
from django.core.serializers.json import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings


def getform(request):
    return render(request, "message_form.html")


def book_list(request):
    db = pymysql.connect(user='root', db='db_book', passwd=settings.DB_PASSWORD, host=settings.DB_HOST)
    cursor = db.cursor()
    cursor.execute("SELECT bookName FROM t_book ORDER BY bookName")
    names = [row[0] for row in cursor.fetchall()]
    db.close()

    content = json.dumps({'status': 'ok', 'data': names}, ensure_ascii=False)
    response = HttpResponse(content, content_type='application/json; charset=utf-8')
    return response
    # return JsonResponse({'status': 'ok', 'data': names})
