# -*- coding: utf-8 -*-
from django.conf.urls import url
from organization.views import TeachersList, OrgList, OrgDetailHomepage, OrgDetailDesc, OrgDetailCourse, \
    OrgDetailTeachers

urlpatterns = [
    url(r'^teachers/list$', TeachersList.as_view(), name="teachers_list"),
    url(r'^list$', OrgList.as_view(), name="org_list"),
    url(r'^home/(?P<org_id>\d+)$', OrgDetailHomepage.as_view(), name="org_detail_homepage"),
    url(r'^desc/(?P<org_id>\d+)$', OrgDetailDesc.as_view(), name="org_detail_desc"),
    url(r'^course/(?P<org_id>\d+)$', OrgDetailCourse.as_view(), name="org_detail_course"),
    url(r'^teacher/(?P<org_id>\d+)$', OrgDetailTeachers.as_view(), name="org_detail_teachers"),

]
