# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$',code_editor,name="compiler"),
    url(r'^result/', result, name="result"),

]
