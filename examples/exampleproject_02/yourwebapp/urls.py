from django.conf.urls.defaults import *
from views import YourModelListView, YourModelUpdateView, YourModelCreateView, YourModelDeleteView

# MODEL URLS
yourmodel_patterns= patterns('',
    url(r'^list/page(?P<page>[0-9]+)/(\?.*)?$', 
        YourModelListView.as_view(),
        name='list'),
    url(r'^update/(?P<pk>\d+)/$', 
        YourModelUpdateView.as_view(),
        name='update'),
    url(r'^create/$', 
        YourModelCreateView.as_view(),
        name='create'),
    url(r'^delete/(?P<pk>[0-9]+)/$', 
        YourModelDeleteView.as_view(),
        name='delete'),
)

newpatterns = patterns('',
    url(r'^yourmodel/', include(yourmodel_patterns, namespace="yourmodel")),
)

try:
    urlpatterns+=newpatterns
except NameError:
    urlpatterns=newpatterns
from django.conf.urls.defaults import *
from views import YourModelListView, YourModelUpdateView, YourModelCreateView, YourModelDeleteView

# MODEL URLS
yourmodel_patterns= patterns('',
    url(r'^list/page(?P<page>[0-9]+)/(\?.*)?$', 
        YourModelListView.as_view(),
        name='list'),
    url(r'^update/(?P<pk>\d+)/$', 
        YourModelUpdateView.as_view(),
        name='update'),
    url(r'^create/$', 
        YourModelCreateView.as_view(),
        name='create'),
    url(r'^delete/(?P<pk>[0-9]+)/$', 
        YourModelDeleteView.as_view(),
        name='delete'),
)

newpatterns = patterns('',
    url(r'^yourmodel/', include(yourmodel_patterns, namespace="yourmodel")),
)

try:
    urlpatterns+=newpatterns
except NameError:
    urlpatterns=newpatterns
