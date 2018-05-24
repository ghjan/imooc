# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
import xadmin

xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion

xversion.register_models()

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^xadmin/', xadmin.site.urls, name='xadmin'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^course/', include('courses.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^org/', include('organization.urls', namespace="organization")),
    url(r'^operation/', include('operation.urls', namespace="operation")),
]

if settings.DEBUG:
    # urlpatterns.extend([url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    #                     # url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    #                     ])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
