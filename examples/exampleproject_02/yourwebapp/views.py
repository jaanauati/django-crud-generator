# Create your views here.
#crudgenerator auto-generated code.
#crudgenetaror date: 14th January 2012 13:52

#modified template

from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from models import YourModel


class YourModelListView(ListView):
    model=YourModel

class YourModelDeleteView(DeleteView):
    model=YourModel
    def get_success_url(self):
        return reverse("yourwebapp:yourmodel:list", args=(1,))

class YourModelCreateView(CreateView):
    model=YourModel
    def get_success_url(self):
        return reverse("yourwebapp:yourmodel:list", args=(1,))

class YourModelUpdateView(UpdateView):
    model=YourModel
    def get_success_url(self):
        return reverse("yourwebapp:yourmodel:list", args=(1,))
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
#crudgenerator auto-generated code.
#crudgenetaror date: 14th January 2012 13:53

#modified template

from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from models import YourModel


class YourModelListView(ListView):
    model=YourModel

class YourModelDeleteView(DeleteView):
    model=YourModel
    def get_success_url(self):
        return reverse("yourwebapp:yourmodel:list", args=(1,))

class YourModelCreateView(CreateView):
    model=YourModel
    def get_success_url(self):
        return reverse("yourwebapp:yourmodel:list", args=(1,))

class YourModelUpdateView(UpdateView):
    model=YourModel
    def get_success_url(self):
        return reverse("yourwebapp:yourmodel:list", args=(1,))
