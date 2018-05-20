# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
import xadmin

xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion

xversion.register_models()

urlpatterns = [
                  url(r'^xadmin/', xadmin.site.urls, name='xadmin'),
                  # url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                  #     {'document_root': settings.STATICFILES_DIRS, 'show_indexes': True}),
                  # url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                  #     {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
