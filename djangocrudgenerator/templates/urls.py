# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from views import *

{{modelname|lower}}_patterns= patterns(
    '',
    url(r'^list/page(?P<page>[0-9]+)/(\?.*)?$',
        {{modelname}}ListView.as_view(),
        name='list'),
    url(r'^update/(?P<pk>\d+)/$',
        {{modelname}}UpdateView.as_view(),
        name='update'),
    url(r'^create/$',
        {{modelname}}CreateView.as_view(),
        name='create'),
    url(r'^delete/(?P<pk>[0-9]+)/$',
        {{modelname}}DeleteView.as_view(),
        name='delete'))


newpatterns = patterns(
    '',
    url(r'^{{modelname|lower}}/', include({{modelname|lower}}_patterns, 
        namespace="{{modelname|lower}}")))


try:
    urlpatterns += newpatterns
except NameError:
    urlpatterns = newpatterns
