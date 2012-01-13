# Create your views here.
#crudgenerator auto-generated code.
#crudgenetaror date: 13th January 2012 15:31

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
#crudgenerator auto-generated code.
#crudgenetaror date: 13th January 2012 15:33

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
#crudgenerator auto-generated code.
#crudgenetaror date: 13th January 2012 15:37
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
