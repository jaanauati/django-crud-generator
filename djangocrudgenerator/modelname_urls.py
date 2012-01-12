
from django.conf.urls.defaults import *

from views import ModelnameListView, ModelnameUpdateView, ModelnameCreateView, ModelnameDeleteView
from django.views.generic import CreateView, ListView
urlpatterns = patterns('',
    url(r'^list/page(?P<page>[0-9]+)/(\?.*)?$', 
        ModelnameListView.as_view(),
        name='list'),
    url(r'^update/(?P<pk>\d+)/$', 
        ModelnameUpdateView.as_view(),
        name='update'),
    url(r'^create/$', 
        ModelnameCreateView.as_view(),
        name='create'),
    url(r'^delete/(?P<pk>[0-9]+)/$', 
        ModelnameDeleteView.as_view(),
        name='delete'),
)
