# -*- coding: utf-8 -*-
from django.conf.urls import url
from courses.views import CoursesListView, CourseDetailView

urlpatterns = [
    url(r'^courses/list$', CoursesListView.as_view(), name="courses_list"),
    url(r'^course/detail/(?P<course_id>\d+)$', CourseDetailView.as_view(), name="course_detail"),

]
