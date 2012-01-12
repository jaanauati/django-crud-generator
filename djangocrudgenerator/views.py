from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from models import Modelname


class ModelnameListView(ListView):
    model=Modelname

class ModelnameDeleteView(DeleteView):
    model=Modelname
    def get_success_url(self):
        return reverse("appname:modelname:list", args=(1,))

class ModelnameCreateView(CreateView):
    model=Modelname
    def get_success_url(self):
        return reverse("appname:modelname:list", args=(1,))

class ModelnameUpdateView(UpdateView):
    model=Modelname
    def get_success_url(self):
        return reverse("appname:modelname:list", args=(1,))

