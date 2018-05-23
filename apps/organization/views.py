from django.shortcuts import render

from django.views.generic.base import View
from .models import CityDict, CourseOrg, Teacher


class TeachersList(View):
    def get(self, request):
        return render(request, 'teachers_list.html', {})


class OrgList(View):
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        all_cities = CityDict.objects.all()

        return render(request, 'org_list.html', {
            "all_orgs": all_orgs,
            "all_cities": all_cities,
        })
