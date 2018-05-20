# _*_ coding: utf-8 _*_
__author__ = 'david'
__date__ = '2018/5/20 23:48'

import xadmin

from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    # 后台列表显示列
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    # 后台列表查询条件
    search_fields = ['name', 'mobile', 'course_name']
    # 后台列表通过时间查询
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


class CourseCommentsAdmin(object):
    # 后台列表显示列
    list_display = ['user', 'course', 'comments', 'add_time']
    # 后台列表查询条件
    search_fields = ['user__name', 'course', 'comments']
    # 后台列表通过时间查询
    list_filter = ['user__name', 'course', 'comments', 'add_time']


class UserFavoriteAdmin(object):
    # 后台列表显示列
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    # 后台列表查询条件
    search_fields = ['user__name', 'fav_id', 'fav_type', ]
    # 后台列表通过时间查询
    list_filter = ['user__name', 'fav_id', 'fav_type', 'add_time']


class UserMessageAdmin(object):
    # 后台列表显示列
    list_display = ['user', 'message', 'has_read', 'add_time']
    # 后台列表查询条件
    search_fields = ['user__name', 'message', 'has_read', ]
    # 后台列表通过时间查询
    list_filter = ['user__name', 'message', 'has_read', 'add_time']


class UserCourseAdmin(object):
    # 后台列表显示列
    list_display = ['user', 'course', 'add_time']
    # 后台列表查询条件
    search_fields = ['user__name', 'course_name', ]
    # 后台列表通过时间查询
    list_filter = ['user__name', 'course_name', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
