# _*_ coding: utf-8 _*_
__author__ = 'david'
__date__ = '2018/5/25 0:13'
from django.shortcuts import render

from django.views.generic.base import View
from organization.models import CourseOrg


class HomepageView(View):
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        return render(request, 'index.html', {"all_orgs": all_orgs})
