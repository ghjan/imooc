# -*- coding: utf-8 -*-
from django.conf.urls import url

import xadmin
from xadmin.plugins import xversion

xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model

xversion.register_models()

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls, name='xadmin'),
]
