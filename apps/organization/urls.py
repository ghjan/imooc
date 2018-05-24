# -*- coding: utf-8 -*-
from django.conf.urls import url
from organization.views import TeachersList, OrgList

urlpatterns = [
    url(r'^teachers/list$', TeachersList.as_view(), name="teachers_list"),
    url(r'^list$', OrgList.as_view(), name="org_list"),
]
