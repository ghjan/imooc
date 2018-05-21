# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
import xadmin

xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion

xversion.register_models()
from django.views.generic import TemplateView
from users.views import LoginView, register, mylogout

urlpatterns = [
                  url(r'^xadmin/', xadmin.site.urls, name='xadmin'),
                  url('^$', TemplateView.as_view(template_name="index.html"), name="index"),
                  url('^login/$', LoginView.as_view(), name="login"),
                  url('^logout/$', mylogout, name="logout"),
                  url('^register/$', register, name="register"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
