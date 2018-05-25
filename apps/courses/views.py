# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import render_to_response
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Course
import traceback


class CoursesListView(View):
    def get(self, request):
        all_courses = Course.objects.all()
        hot_courses = Course.objects.order_by("-click_num")[:3]
        sort = request.GET.get("sort", "")
        if sort:
            if sort == "students":
                all_courses = all_courses.order_by('-students')
            elif sort == "click_num":
                all_courses = all_courses.order_by('-click_num')

        # paginator = Paginator(all_courses, 3, request=request)
        paginator = Paginator(all_courses, 9)
        try:
            page = request.GET.get('page', 1)
        except:
            page = 1
        try:
            courses = paginator.page(page)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            courses = paginator.page(paginator.num_pages)

        # course_nums = len(all_courses)
        try:
            return render(request, 'courses_list.html', {
                'list_view': 'courses',
                "all_courses": courses,
                # "course_nums": course_nums,
                "hot_courses": hot_courses,
                "sort": sort,
            })
        except Exception as e:
            print(e)
            traceback.print_exc()


class CourseDetailView(View):
    def get(self, request):
        return render(request, 'course-detail.html', {})
