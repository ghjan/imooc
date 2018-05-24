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
        hot_orgs = CourseOrg.objects.order_by("-click_num")[:3]
        all_cities = CityDict.objects.all()
        all_ct = dict((("pxjg", "培训机构"), ("gr", "个人"), ("gx", "高校"),))

        city_id = request.GET.get('city', "")
        if city_id:
            all_orgs = all_orgs.filter(city__id=int(city_id))

        ct = request.GET.get('ct', "")
        if ct:
            all_orgs = all_orgs.filter(category=ct)

        sort = request.GET.get("sort", "")
        if sort:
            if sort == "students":
                all_orgs.order_by("-students")
            elif sort == "courses":
                all_orgs.order_by("-course_num")
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
            "city_id": city_id,
            "all_ct": all_ct,
            "ct": ct,
            "hot_orgs": hot_orgs,
            "sort": sort,
        })
