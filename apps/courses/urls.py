# -*- coding: utf-8 -*-
from django.conf.urls import url
from courses.views import CoursesListView

urlpatterns = [
    url(r'^courses/list$', CoursesListView.as_view(), name="courses_list"),
]
