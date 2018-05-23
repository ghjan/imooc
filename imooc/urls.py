# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
import xadmin

xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion

xversion.register_models()
from django.views.generic import TemplateView
from users.views import LoginView, RegisterView, LogoutView, UsercenterView, ActivateUserView, ForgetpwdView, \
    ResetView, SetpwdView
from courses.views import CoursesListView
from organization.views import TeachersList, OrgList

urlpatterns = [
                  url(r'^xadmin/', xadmin.site.urls, name='xadmin'),
                  url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
                  url(r'^login/$', LoginView.as_view(), name="login"),
                  url(r'^logout/$', LogoutView.as_view(), name="logout"),
                  url(r'^register/$', RegisterView.as_view(), name="register"),
                  url(r'^forgetpwd/$', ForgetpwdView.as_view(), name="forgetpwd"),
                  url(r'^activate/(?P<code>\w+)/$', ActivateUserView.as_view()),
                  url(r'^reset/(?P<code>\w+)/$', ResetView.as_view(), name="resetpwd"),
                  url(r'^setpwd/$', SetpwdView.as_view(), name="setpwd"),
                  url(r'^usercenter-info/$', UsercenterView.as_view(), name="usercenter-info"),
                  url(r'^captcha/', include('captcha.urls')),
                  url(r'^courses/list$', CoursesListView.as_view(), name="courses_list"),
                  url(r'^teachers/list$', TeachersList.as_view(), name="teachers_list"),
                  url(r'^org/list$', OrgList.as_view(), name="org_list"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
