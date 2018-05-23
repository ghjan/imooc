from django.shortcuts import render

from django.views.generic.base import View
from .models import CityDict, CourseOrg, Teacher
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


class TeachersList(View):
    def get(self, request):
        return render(request, 'teachers_list.html', {})


class OrgList(View):
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        all_cities = CityDict.objects.all()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # Provide Paginator with the request object for complete querystring generation
        p = Paginator(all_orgs, 2, request=request)
        orgs = p.page(page)
        org_nums = len(all_orgs)
        return render(request, 'org_list.html', {
            "all_orgs": orgs,
            "all_cities": all_cities,
            "org_nums": org_nums,
        })
