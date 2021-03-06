# _*_ coding: utf-8 _*_
__author__ = 'david'
__date__ = '2018/5/20 10:31'

import xadmin
from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    # 后台列表显示列
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_num', 'click_num', 'add_time','course_org']
    # 后台列表查询条件
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_num', 'click_num', 'course_org__name']
    # 后台列表通过时间查询
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_num', 'click_num', 'add_time', 'course_org__name']


class LessonAdmin(object):
    # 后台列表显示列
    list_display = ['course', 'name', 'add_time']
    # 后台列表查询条件
    search_fields = ['course__name', 'name']
    # 后台列表通过时间查询
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    # 后台列表显示列
    list_display = ['lesson', 'name', 'add_time']
    # 后台列表查询条件
    search_fields = ['lesson__name', 'name']
    # 后台列表通过时间查询
    list_filter = ['lesson__name', 'name', 'add_time']


class CourseResourceAdmin(object):
    # 后台列表显示列
    list_display = ['course', 'name', 'download', 'add_time']
    # 后台列表查询条件
    search_fields = ['course__name', 'download', 'name']
    # 后台列表通过时间查询
    list_filter = ['course__name', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
